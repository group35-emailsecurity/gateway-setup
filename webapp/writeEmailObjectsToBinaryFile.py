import pickle
from models.email import Email

emailList = []
count = 0

def writeToBinaryFileFromEmailList(writeBinFilePath, writeEmailList):
    # Write list to bin file
    with open(writeBinFilePath, "wb") as f:
        pickle.dump(writeEmailList, f)

def readFromBinaryFileToEmailList(readBinFilePath):
    global count
    # Open binary file using pickle
    with open(readBinFilePath, "rb") as f:
        readEmailList = pickle.load(f)
        
        for email in readEmailList:
            count += 1
    
    return readEmailList

#Get Current Email Records
emailList = readFromBinaryFileToEmailList('data/emails.bin')

userInput = ""
print("Welcome to email object utility program!")
userInput = str(input("Please press 'Y' to add an email object: "))

while userInput.lower() == "y":
    count += 1
    emailId = count
    emailToAddress = input("Please enter email to address: ")
    emailFromAddress = input("Please enter email from address: ")
    emailSubject = input("Please enter email subject: ")
    emailBody = input("Please enter email body: ")

    newEmail = Email(emailId, emailToAddress, emailFromAddress, emailSubject, emailBody)
    emailList.append(newEmail)
    userInput = str(input("Please press 'Y' to add ANOTHER email object: "))

#Write new email records to bin file
writeToBinaryFileFromEmailList("data/emails.bin", emailList)

#Display list of email records saved
for email in emailList:
    emailOutput = str(email.id) +  " " + email.toAddress + " " + email.fromAddress + " " + email.subject + " " + email.body
    print(emailOutput)