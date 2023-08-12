import os
import pickle
from models.log import Log

count = 0

def writeToBinaryFileFromLogList(writeBinFilePath, writeLogList):
    # Check if writeLogList contains records
    if(writeLogList != []):
        # open new bin file
        with open(writeBinFilePath, "wb") as f:
            pickle.dump(writeLogList, f)

def readFromBinaryFileToLogList(readBinFilePath):
    global count
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
                    count += 1
                    logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject + " " + log.message + " " + log.action
                    print(logOutput) 

    else:
        print("File does NOT exist")
        print("Creating new empty bin file")

        file = open(readBinFilePath,"x")
        file.close()

        print("New empty bin file created")

    return readLogList

print("Welcome to log record utlity program!")

#Get Current Log Records
logList = readFromBinaryFileToLogList('data/logs.bin')

userInput = str(input("Please press 'Y' to add an log record: "))

while userInput.lower() == "y":
    if(userInput.lower() == "y"):
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
writeToBinaryFileFromLogList("data/logs.bin", logList)

if(logList == []):
    print("No records to display")
else:
    #Display list of log records saved
    for log in logList:
        logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject +  " " + log.message + " " + log.action
        print(logOutput)