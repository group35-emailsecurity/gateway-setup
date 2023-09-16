#!/usr/bin/env python
import email
import re
import sys
import re
import random
import string
import utilities
from models.email import Email
from models.log import Log
from datetime import date
from datetime import time
from enum import Enum
from subprocess import run
from email import policy

# This script must return an exit code of 0 or 1
# Exit code 0: No threat detected. This exit code will result in the email being delivered to the intended recipient.
# Exit code 1: Threat detected. This exit code will result in the email being discarded.

# Generate random string to facilitate synchronous filter service operations
randomChars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

class Outcome(Enum):
    ALLOWED = 0
    DENIED = 1

# Raw email in string format
emailStr = sys.stdin.read()

# Email in object form with each element (To, From, Subject, etc.) mapped to an object property.
emailObj = email.message_from_string(emailStr, policy=email.policy.default)

# Get 'from' address
fromDetails = emailObj['From']
emailFromregex = r'<([^>]+)>'
match = re.search(emailFromregex, fromDetails)
emailFromAddress = match.group(1)

# Get other elements
emailToAddress = emailObj['To']
emailSubject = emailObj['Subject']
emailBody = emailObj.get_body(('plain',)).get_content()

exitCode = Outcome.ALLOWED.value

domainRegex = r'@(.*)'
if re.findall(domainRegex, emailFromAddress)[0] == "internal.test":
    # Outbound emails logic
    # Keyword list scanning for outgoing emails
    logMessage = "OUTBOUND: No encryption required. No sensitive words detected."
    protectedKeywordList = ["secret", "confidential", "private"]
    for keyword in protectedKeywordList:
        if re.search(keyword, emailBody, re.IGNORECASE):
            logMessage = "OUTBOUND: Encrypting email. Sensitive word '%s' detected." % keyword
            
            # Give the email a new body, overwriting the old one
            newBody = "Encrypted message attached"
            emailObj.set_content(newBody)

            # Pipe oldBody into gpg and save symetrically encrypted file that will be attached to the email
            encryptedAttachmentPath = f'/home/user/encrypted-{randomChars}.gpg'
            gpgPassphrase = "open"
            run(['gpg', '--output', encryptedAttachmentPath, '--symmetric', '--passphrase', gpgPassphrase, '--batch', '--yes'], input=emailBody, text=True)

            # Get encrypted file
            with open(encryptedAttachmentPath, 'rb') as file:
                data = file.read()

            # Attach encrypted file to email
            emailObj.add_attachment(data, maintype='application', subtype='octet-stream', filename="encrypted.gpg")

            # Overwrite the original email with the new version. New version will be piped back into postfix via filter-handler.sh for delivery
            emailFilePath = sys.argv[1]
            with open(emailFilePath, 'w') as file:
                file.write(emailObj.as_string())

            # Delete encrypted file
            run(['rm', encryptedAttachmentPath])
            
            break

else:
    # Inbound emails logic
    keywordBlacklist = ["casino", "lottery", "viagra"]
    emailOutcome = Outcome.ALLOWED.name
    logMessage = "INBOUND: Email allowed. No suspicious words or attachments detected."

    # Keyword scanning
    for keyword in keywordBlacklist:
        if re.search(keyword, emailStr, re.IGNORECASE):
            emailOutcome = Outcome.DENIED.name
            exitCode = Outcome.DENIED.value
            logMessage = "INBOUND: Email denied. Suspicious word '%s' detected." % keyword
            break

    # Attachment scanning
    attachmentsDirectoryPath = f'/home/user/attachments-{randomChars}/'
    run(['ripmime', '-i', '-', '-d', attachmentsDirectoryPath], input=emailStr, text=True)  # Extract attachments
    scanResult = run(['clamdscan', '--stream', attachmentsDirectoryPath], capture_output=True, text=True).stdout  # Scan attachments
    run(['rm', '-r', attachmentsDirectoryPath])  # Delete extracted attachments directory
    infectedCount = re.findall(r'Infected files: (.+)', scanResult)[0]  # Get infected attachment count

    if infectedCount != "0":
        emailOutcome = Outcome.DENIED.name
        exitCode = Outcome.DENIED.value
        logMessage = "INBOUND: Email denied. Suspicious attachment detected."

    # Create and Add Email record
    emailCount = utilities.getEmailListCount('../../webapp/data/emails.bin')
    emailCount += 1
    emailId = emailCount

    # Create Email Object
    emailRecord = Email(emailId, emailToAddress, emailFromAddress, emailSubject, emailBody, emailStr)

    # Get current email records and add Email record to list
    emailList = []
    emailList = utilities.readFromBinaryFileToEmailList('../../webapp/data/emails.bin', emailList)
    emailList.append(emailRecord)

    # Write the updated Email List to bin file
    utilities.writeToBinaryFileFromEmailList('../../webapp/data/emails.bin')
    #################################### Create email record   ########################################

    # TODO: Add To, From and subject from Email variable
    #################################### Create new Log Record ########################################
    # Create and Add Log record
    logCount = utilities.getLogListCount('../../webapp/data/logs.bin')
    logCount += 1
    logId = logCount
    logDate = date.today()
    logTime = "11:32"
    logTo = "user@group35.com"
    logFrom = "admin@group35.com"
    logSubject = "Please meet in boardroom at 1PM"

    # Create Log object
    logRecord = Log(logId, logDate, logTime, logTo, logFrom, logSubject, logMessage, emailOutcome)

    # Get current log records and add Log record to list
    logList = []
    logList = utilities.readFromBinaryFileToLogList('../../webapp/data/logs.bin')
    logList.append(logRecord)

    # Write the updated Log List to bin file
    utilities.writeToBinaryFileFromLogList('../../webapp/data/logs.bin', logList)
    #################################### Create new Log Record ########################################
    
print(logMessage)

sys.exit(exitCode)
