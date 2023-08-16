# This file is used to create Email and Log records by using a terminal menu system
import writeEmailObjectsToBinaryFile
import writeLogObjectsToBinaryFile

def displayAllEmailRecords():
    writeEmailObjectsToBinaryFile.displayAllEmailRecords('data/emails.bin')

def displayAllLogRecords():
    writeLogObjectsToBinaryFile.displayAllLogRecords('data/logs.bin')

def addEmailRecord():
    writeEmailObjectsToBinaryFile.addEmailRecord('data/emails.bin')

def addLogRecord():
    writeLogObjectsToBinaryFile.addLogRecord('data/logs.bin')

print("\nWelcome to utility program for creating records, please choose one of the following options")
print("\nMain Menu")
print("1. Display all email records")
print("2. Display all log records")
print("3. Add email record")
print("4. Add log record")
print("5. Exit program")

userInput = int(input("Enter menu selection number: "))
while userInput != 5:
    if(userInput != 5):
        if(userInput == 1):
            displayAllEmailRecords()
        elif(userInput == 2):
            displayAllLogRecords()
        elif(userInput == 3):
            addEmailRecord()
        elif(userInput == 4):
            addLogRecord()
        else:
            print("Invalid menu option, please try again")
    else:
        break
    print("\nMain Menu")
    print("1. Display all email records")
    print("2. Display all log records")
    print("3. Add email record")
    print("4. Add log record")
    print("5. Exit program")
    userInput = int(input("Enter menu selection number: "))

