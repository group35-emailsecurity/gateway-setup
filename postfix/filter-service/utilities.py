from models.email import Email
from models.log import Log
import pickle
import os

def displayAllLogRecords(filePath):
    logList = readFromBinaryFileToLogList(filePath)

    if(logList == []):
        print("No records to display")
    else:
        #Display list of log records saved
        for log in logList:
            logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject +  " " + log.message + " " + log.action
            print(logOutput)

def writeToBinaryFileFromLogList(writeBinFilePath, writeLogList):
    # Check if writeLogList contains records
    if(writeLogList != []):
        if(os.path.exists(writeBinFilePath)):
            # Write list to existing bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeLogList, f)
        else:
            newDirectory = os.path.dirname(writeBinFilePath)
            doesDirectoryExist = os.path.exists(newDirectory)
            if not doesDirectoryExist:
                print("Directory does NOT exist")
                os.makedirs(newDirectory)
                print("Directory has been created")

            # Write list to new bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeLogList, f)

def readFromBinaryFileToLogList(readBinFilePath):
    global count
    readLogList = []

    # Try to open file if it exists
    if(os.path.exists(readBinFilePath)):
        print("File does exist")

        if(os.stat(readBinFilePath).st_size == 0):
            print("File is empty, cannot open file")
        else:
            print("Opening file to get records")
            # Open binary file using pickle
            with open(readBinFilePath, "rb") as f:
                readLogList = pickle.load(f)

    else:
        newDirectory = os.path.dirname(readBinFilePath)
        doesDirectoryExist = os.path.exists(newDirectory)
        if not doesDirectoryExist:
            print("Directory does NOT exist")
            os.makedirs(newDirectory)
            print("Directory has been created")

        print("File does NOT exist")
        print("Creating new empty bin file")

        file = open(readBinFilePath,"x")
        file.close()

        print("New empty bin file created")

    return readLogList

def getLogListCount(filePath):
    count = 0
    logList = readFromBinaryFileToLogList(filePath)
    
    if(logList != []):
        #Count records stored in bin file
        for log in logList:
            count += 1
    
    return count


def addLogRecord(filePath):
    #Get Current Log Records
    logList = readFromBinaryFileToLogList(filePath)

    userInput = str(input("Please press 'Y' to add an log record: "))

    while userInput.lower() == "y":
        if(userInput.lower() == "y"):
            count = getLogListCount(filePath)
            count += 1
            logId = count
            logDate = input("Please enter date(YYYY-MM-DD): ")
            logTime = input("Please enter time (24H): ")
            logTo = input("Please enter to address: ")
            logFrom = input("Please enter from address: ")
            logSubject = input("Please enter email subject: ")
            logMessage = input("Please enter enter log message: ")
            logAction = input("Please enter the action taken: ")
            newLog = Log(logId, logDate, logTime, logTo, logFrom, logSubject, logMessage, logAction)
            logList.append(newLog)
            userInput = str(input("Please press 'Y' to add ANOTHER log record: "))
        else:
            break
    
        #Write new log records to bin file
        writeToBinaryFileFromLogList(filePath, logList)

#readFromBinaryFileToLogList('../../webapp/data/logs.bin')
#displayAllLogRecords('../../webapp/data/logs.bin')

def displayAllEmailRecords(filePath):
    emailList = readFromBinaryFileToEmailList(filePath)
    
    if(emailList == []):
        print("No records to display")
    else:
        #Display list of email records saved
        for email in emailList:
            emailOutput = str(email.id) +  " " + email.toAddress + " " + email.fromAddress + " " + email.subject + " " + email.body
            print(emailOutput)
    

def writeToBinaryFileFromEmailList(writeBinFilePath, writeEmailList):
    # Check if writeEmailList contains records
    if(writeEmailList != []):
        if(os.path.exists(writeBinFilePath)):
            # Write list to existing bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeEmailList, f)
        else:
            doesDirectoryExist = os.path.exists(writeBinFilePath)
            if not doesDirectoryExist:
                print("Directory does NOT exist")
                newDirectory = os.path.dirname(writeBinFilePath)
                os.makedirs(newDirectory)
                print("Directory has been created")

            # Write list to new bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeEmailList, f)
            

def readFromBinaryFileToEmailList(readBinFilePath):
    global count
    readEmailList = []

    # Try to open file if it exists
    if(os.path.exists(readBinFilePath)):
        print("File does exist")

        if(os.stat(readBinFilePath).st_size == 0):
            print("File is empty, cannot open file")
        else:
            print("Opening file to get records")
            # Open binary file using pickle
            with open(readBinFilePath, "rb") as f:
                readEmailList = pickle.load(f)

        return readEmailList
    else:
        newDirectory = os.path.dirname(readBinFilePath)
        doesDirectoryExist = os.path.exists(newDirectory)
        if not doesDirectoryExist:
            print("Directory does NOT exist")
            os.makedirs(newDirectory)
            print("Directory has been created")
            
        print("File does NOT exist")
        print("Creating new empty bin file")

        file = open(readBinFilePath,"x")
        file.close()

        print("New empty bin file created")

    return readEmailList

def getEmailListCount(filePath):
    count = 0
    emailList = readFromBinaryFileToEmailList(filePath)
    
    if(emailList != []):
        #Count records stored in bin file
        for email in emailList:
            count += 1
    
    return count

def addEmailRecord(filePath):
    #Get Current Email Records
    emailList = readFromBinaryFileToEmailList(filePath)

    userInput = str(input("Please press 'Y' to add an email object: "))

    while userInput.lower() == "y":
        if(userInput.lower() == "y"):
            count = getEmailListCount(filePath)
            count += 1
            emailId = count
            emailToAddress = input("Please enter email to address: ")
            emailFromAddress = input("Please enter email from address: ")
            emailSubject = input("Please enter email subject: ")
            emailBody = input("Please enter email body: ")

            newEmail = Email(emailId, emailToAddress, emailFromAddress, emailSubject, emailBody)
            emailList.append(newEmail)
            userInput = str(input("Please press 'Y' to add ANOTHER email object: "))
        else:
            break

        #Write new email records to bin file
        writeToBinaryFileFromEmailList(filePath, emailList)


#readFromBinaryFileToEmailList('../../webapp/data/emails.bin')
#displayAllEmailRecords('../../webapp/data/emails.bin')