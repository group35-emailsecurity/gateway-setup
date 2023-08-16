import os
import pickle
from models.email import Email

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
        # Write list to existing bin file
        with open(writeBinFilePath, "wb") as f:
            pickle.dump(writeEmailList, f)

def readFromBinaryFileToEmailList(readBinFilePath):
    global count
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

        return readEmailList
    else:
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
