from flask import Flask, render_template, url_for
import csv
import json
import os
import pickle
from models.email import Email
from models.log import Log

app = Flask(__name__)

def writeToBinaryFileFromEmailList(writeBinFilePath, writeEmailList):
    # Creat list and email objects for testing
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
    if(writeEmailList == False):
        print("Error with log list, log list is empty or invalid")
    else:
        # Check if the file exists, if not create a new bin file
        if(os.path.exists(writeBinFilePath)):
            # Write list to existing bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeEmailList, f)
        else:
            # Create new bin file
            file = open(writeBinFilePath,"x")
            file.close()

            # open new bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeEmailList, f)

def readFromBinaryFileToEmailList(readBinFilePath):
    # Try to open file if it exists
    try:
        # Open binary file using pickle
        with open(readBinFilePath, "rb") as f:
            readEmailList = pickle.load(f)

            # print("\n\nEmail list")
            # for email in readEmailList:
            #    emailOutput = str(email.id) +  " " + email.toAddress + " " + email.fromAddress + " " + email.subject + " " + email.body
            #    print(emailOutput)
        
        return readEmailList
    except:
        print("Unable to open file, please check the file location")

    return False

def writeToBinaryFileFromLogList(writeBinFilePath, writeLogList):
    # Create list and log objects
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
    if(writeLogList == False):
        print("Error with log list, log list is empty or invalid")
    else:
        # Check if the file exists, if not create a new bin file
        if(os.path.exists(writeBinFilePath)):
            # Write list to existing bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeLogList, f)
        else:
            # Create new bin file
            file = open(writeBinFilePath,"x")
            file.close()

            # open new bin file
            with open(writeBinFilePath, "wb") as f:
                pickle.dump(writeLogList, f)

def readFromBinaryFileToLogList(readBinFilePath):
    readLogList = []

    # Try to open file if it exists
    try:
        # Open binary file using pickle
        with open(readBinFilePath, "rb") as f:
            readLogList = pickle.load(f)

            # print("\n\nLog List")
            # for log in readLogList:
            #    logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject +  " " + log.message + " " + log.action
            #    print(logOutput)
        
        return readLogList
    except:
        print("Unable to open file, please check the file location")
    
    return False
        
@app.route('/')
def index():
    pieChartData = {'Task' : 'Total emails', 'Allowed' : 234, 'Blocked' : 153, 'Quarantine' : 86}
    barChartData = {'Task' : 'Threats found', 'Virus' : 57, 'Spam' : 56, 'Phishing' : 40}
    #print(data)
    
    return render_template('index.html', pieChartData = pieChartData, barChartData = barChartData)

@app.route('/emails')
def emails():
    # writeToBinaryFileFromEmailList('data/emails.bin')
    headings = ("ID","To","From","Subject","Body")
    emailData = readFromBinaryFileToEmailList('data/emails.bin')
    return render_template('emails.html',emailData = emailData,headings = headings)

@app.route('/logs')
def logs():
    # writeToBinaryFileFromLogList('data/logs.bin')
    headings = ("ID","Date","Time","To","From","Subject", "Message", "Action")
    logData = readFromBinaryFileToLogList('data/logs.bin')
    return render_template('logs.html', logData = logData, headings = headings)

@app.route('/login')
def login():
    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)
