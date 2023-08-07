import pickle
from models.log import Log

logList = []
count = 0

def writeToBinaryFileFromLogList(writeBinFilePath, writeLogList):
    # Write list to bin file
    with open(writeBinFilePath, "wb") as f:
        pickle.dump(writeLogList, f)

def readFromBinaryFileToLogList(readBinFilePath):
    global count
    # Open binary file using pickle
    with open(readBinFilePath, "rb") as f:
        readLogList = pickle.load(f)
        
        for log in readLogList:
            count += 1
    
    return readLogList

#Get Current Log Records
logList = readFromBinaryFileToLogList('data/logs.bin')

userInput = ""
print("Welcome to log record utlity program!")
userInput = str(input("Please press 'Y' to add an log record: "))

while userInput.lower() == "y":
    count += 1
    logId = count
    logDate = input("Please enter date(YYYY-MM-DD): ")
    logTime = input("Please enter time (24H): ")
    logTo = input("Please enter to address: ")
    logFrom = input("Please enter from address: ")
    logSubject = input("Please enter email subject: ")
    logAction = input("Please enter the action taken: ")

    newLog = Log(logId, logDate, logTime, logTo, logFrom, logSubject, logAction)
    logList.append(newLog)
    userInput = str(input("Please press 'Y' to add ANOTHER log record: "))

#Write new log records to bin file
writeToBinaryFileFromLogList("data/logs.bin", logList)

#Display list of log records saved
for log in logList:
    logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject + " " + log.action
    print(logOutput)