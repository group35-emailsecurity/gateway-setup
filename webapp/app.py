from flask import Flask, render_template, url_for
import csv
import json
import pickle
from models.email import Email
from models.log import Log

app = Flask(__name__)

def csvToEmailList(csvFilePath):
    #create list to store email objects
    emailList = []
 
    #open csv file and read in email data
    with open(csvFilePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            emailList.append(Email(row[0], row[1], row[2],row[3],row[4]))
    
        #print(emailList)
        return emailList
    
def csvToLogList(csvFilePath):
    #create list to store log objects
    logList = []

    #open csv file and read in log data
    with open(csvFilePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            logList.append(Log(row[0], row[1], row[2],row[3],row[4],row[5],row[6]))

        #print(emailList)
        return logList

def writeToBinaryFileFromEmailList(writeBinFilePath):
    # Creat list and email objects
    writeEmailList = []
    email1 = Email(1,"asfasdf@gmail.com","user@group35.com","You have won the lottery"," 	Dear sir madam you have won the lottery please provide your bank login account to claim your winnings")
    email2 = Email(2, "test@gmail.com","user@group35.com","This is a test"," 	Dear sir/madam this is a valid test email that is safe")
    email3 = Email(3, "fasdfafdsf@gmail.com", "user@group35.com", "Please confirm PayPal deatils" ,"Dear sir please enter your paypal deatils")
    email4 = Email(4, "group35@mail.com","bob@gmail.com","You have won the UK Lotto","Please provide your banking details for your lottery winnings")

    # Append email objects to list
    writeEmailList.append(email1)
    writeEmailList.append(email2)
    writeEmailList.append(email3)
    writeEmailList.append(email4)

    # Write list to bin file
    with open(writeBinFilePath, "wb") as f:
        pickle.dump(writeEmailList, f)

def readFromBinaryFileToEmailList(readBinFilePath):
    # Open binary file using pickle
    with open(readBinFilePath, "rb") as f:
        readEmailList = pickle.load(f)

    # for email in readEmailList:
        # emailOutput = str(email.id) +  " " + email.toAddress + " " + email.fromAddress + " " + email.subject + " " + email.body
        # print(emailOutput)
    
    return readEmailList

def writeToBinaryFileFromLogList(writeBinFilePath):
    # Create list and log objects
    writeLogList = []
    log1 = Log(1,"2023-02-23", "11:12", "user@group35.com", "hacker@gmail.com", "Please provide paypal details", "Blocked")
    log2 = Log(2,"2023-03-28", "14:32", "admin@group35.com", "user@group35.com", "This is a test email that is safe", "Allowed")
    log3 = Log(3,"2023-04-18", "09:32", "user3@group35.com", "adfasdfads@gmail.com", "Please provide Click this link to get your winnings", "Blocked")
    log4 = Log(4,"2023-05-17", "19:01", "user5@group35.com", "admin@group35.com", "Can you please meet me at lunchtime", "Allowed")

    # Append log objects to list
    writeLogList.append(log1)
    writeLogList.append(log2)
    writeLogList.append(log3)
    writeLogList.append(log4)

    # Write log list to file
    with open(writeBinFilePath, "wb") as f:
        pickle.dump(writeLogList, f)

def readFromBinaryFileToLogList(readBinFilePath):
    # Open binary file using pickle
    with open(readBinFilePath, "rb") as f:
        readLogList = pickle.load(f)

    # for log in readLogList:
        # logOutput = str(log.id) +  " " + log.date + " " + log.time + " " + log.toAddress + " " + log.fromAddress + " " + log.subject + " " + log.action
        # print(logOutput)
    
    return readLogList
        
@app.route('/')
def index():
    pieChartData = {'Task' : 'Total emails', 'Allowed' : 234, 'Blocked' : 153, 'Quarantine' : 86}
    barChartData = {'Task' : 'Threats found', 'Virus' : 57, 'Spam' : 56, 'Phishing' : 40}
    #print(data)
    
    return render_template('index.html', pieChartData = pieChartData, barChartData = barChartData)

@app.route('/emails')
def emails():
    # writeToBinaryFileFromEmailList('data/emails.bin')
    headings = ("ID","From","To","Subject","Body")
    emailData = readFromBinaryFileToEmailList('data/emails.bin')
    return render_template('emails.html',emailData = emailData,headings = headings)

@app.route('/logs')
def logs():
    # writeToBinaryFileFromLogList('data/logs.bin')
    headings = ("ID","Date","Time","From","To","Subject","Action")
    logData = readFromBinaryFileToLogList('data/logs.bin')
    return render_template('logs.html', logData = logData, headings = headings)

if __name__ == "__main__":
    app.run(debug=True)
