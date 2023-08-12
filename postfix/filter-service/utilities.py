from models.email import Email
from models.log import Log
import pickle
import os

logCount = 0
emailCount = 0

def writeToBinaryFileFromEmailList(writeBinFilePath, writeEmailList):
    # Check if writeEmailList contains records
    if(writeEmailList != []):
        # Write list to existing bin file
        with open(writeBinFilePath, "wb") as f:
            pickle.dump(writeEmailList, f)

def writeToBinaryFileFromEmailList(writeBinFilePath):
    # Creat list and email objects
    writeEmailList = []
    email1 = Email(1,"user@group35.com","asfasdf@gmail.com","You have won the lottery"," 	Dear sir madam you have won the lottery please provide your bank login account to claim your winnings")
    email2 = Email(2, "user@group35.com","test@gmail.com","This is a test"," 	Dear sir/madam this is a valid test email that is safe")
    email3 = Email(3, "user@group35.com", "fasdfafdsf@gmail.com", "Please confirm PayPal deatils" ,"Dear sir please enter your paypal deatils")
    email4 = Email(4, "group35@mail.com","bob@gmail.com","You have won the UK Lotto","Please provide your banking details for your lottery winnings")

    # Append email objects to list
    writeEmailList.append(email1)
    writeEmailList.append(email2)
    writeEmailList.append(email3)
    writeEmailList.append(email4)

    # Check if writeEmailList contains records
    if(writeEmailList != []):
        # Write list to existing bin file
        with open(writeBinFilePath, "wb") as f:
            pickle.dump(writeEmailList, f)
    
def readFromBinaryFileToEmailList(readBinFilePath):
    global emailCount
    readEmailList = []

    # Try to open file if it exists
    if(os.path.isfile(readBinFilePath)):
        print("File does exist")
        if(os.stat(readBinFilePath).st_size == 0):
            print("File is empty, cannot open file")
        else:
            print("Opening file to get records")
            # Open binary file using pickle
            with open(readBinFilePath, "rb") as f:
                readEmailList = pickle.load(f)

                print("\n\nEmail list")
                for email in readEmailList:
                    emailCount += 1
                    emailOutput = str(email.id) +  " " + email.toAddress + " " + email.fromAddress + " " + email.subject + " " + email.body
                    print(emailOutput)
        
        return readEmailList
    else:
        print("File does NOT exist")
        print("Creating new empty bin file")

        file = open(readBinFilePath,"x")
        file.close()

        print("New empty bin file created")

    return readEmailList

def writeToBinaryFileFromLogList(writeBinFilePath, writeLogList):
    # Check if writeLogList contains records
    if(writeLogList != []):
        # open new bin file
        with open(writeBinFilePath, "wb") as f:
            pickle.dump(writeLogList, f)

def writeToBinaryFileFromLogList(writeBinFilePath):
    # Create list and log objects
    writeLogList = []
    log1 = Log(1,"2023-02-23", "11:12", "user@group35.com", "hacker@gmail.com", "Please provide paypal details", "Phishing attack","Blocked")
    log2 = Log(2,"2023-03-28", "14:32", "admin@group35.com", "user@group35.com", "This is a test email that is safe", "No issues found with email ", "Allowed")
    log3 = Log(3,"2023-04-18", "09:32", "user3@group35.com", "adfasdfads@gmail.com", "Please provide Click this link to get your winnings", "Phishing attack ", "Blocked")
    log4 = Log(4,"2023-05-17", "19:01", "user5@group35.com", "admin@group35.com", "Can you please meet me at lunchtime", "No issues found with email", "Allowed")

    # Append log objects to list
    writeLogList.append(log1)
    writeLogList.append(log2)
    writeLogList.append(log3)
    writeLogList.append(log4)

    # Check if writeLogList contains records
    if(writeLogList != []):
        # open new bin file
        with open(writeBinFilePath, "wb") as f:
            pickle.dump(writeLogList, f)

def readFromBinaryFileToLogList(readBinFilePath):
    global logCount
    readLogList = []

    # Try to open file if it exists
    if(os.path.isfile(readBinFilePath)):
        print("File does exist")
        if(os.stat(readBinFilePath).st_size == 0):
            print("File is empty, cannot open file")
        else:
            print("Opening file to get records")
            # Open binary file using pickle
            with open(readBinFilePath, "rb") as f:
                readLogList = pickle.load(f)

                print("\n\nLog List")
                for log in readLogList:
                    logCount += 1
                    logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject + " " + log.message + " " + log.action
                    print(logOutput) 
    else:
        print("File does NOT exist")
        print("Creating new empty bin file")

        file = open(readBinFilePath,"x")
        file.close()

        print("New empty bin file created")

    return readLogList

def readListCount(readBinFilePath):
    count = 0
    # Try to open file if it exists
    if(os.path.isfile(readBinFilePath)):
        print("File does exist")
        if(os.stat(readBinFilePath).st_size == 0):
            print("File is empty, cannot open file")
        else:
            print("Opening file to get records")
            # Open binary file using pickle
            with open(readBinFilePath, "rb") as f:
                readLogList = pickle.load(f)

                for log in readLogList:
                    count += 1
    else:
        print("File does NOT exist")
        print("Cannot calculate record count")

    return count

writeToBinaryFileFromEmailList('../../webapp/data/emails.bin')
writeToBinaryFileFromLogList('../../webapp/data/logs.bin')

readFromBinaryFileToEmailList('../../webapp/data/emails.bin')
readFromBinaryFileToLogList('../../webapp/data/logs.bin')