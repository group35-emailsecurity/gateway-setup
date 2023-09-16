from flask import Flask, render_template, url_for
import json
import os
import pickle
import writeEmailObjectsToBinaryFile
import writeLogObjectsToBinaryFile
from email import policy
from email.parser import Parser
from models.email import Email
from models.log import Log

app = Flask(__name__)


@app.route('/')
def index():
    # pieChartData = {'Task' : 'Total emails', 'Allowed' : 234, 'Blocked' : 153, 'Quarantine' : 86}
    pieChartData = writeLogObjectsToBinaryFile.getLogListActionCount(
        'data/logs.bin')
    barChartData = writeLogObjectsToBinaryFile.getLogListTypeCount(
        'data/logs.bin')
    # barChartData = {'Task' : 'Threats found', 'Virus' : 57, 'Spam' : 56, 'Phishing' : 40}
    # print(data)

    return render_template('index.html', pieChartData=pieChartData, barChartData=barChartData)


@app.route('/emails')
def emails():
    headings = ("ID", "To", "From", "Subject", "Body", "Open")
    emailData = writeEmailObjectsToBinaryFile.readFromBinaryFileToEmailList(
        'data/emails.bin')
    
    


    return render_template('emails.html', emailData=emailData, headings=headings)


@app.route('/logs')
def logs():
    headings = ("ID", "Date", "Time", "To", "From",
                "Subject", "Message", "Type", "Action")
    logData = writeLogObjectsToBinaryFile.readFromBinaryFileToLogList(
        'data/logs.bin')
    return render_template('logs.html', logData=logData, headings=headings)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')

@app.route('/displayEmail/<id>')
def displayEmail(id):
    originalEmail = writeEmailObjectsToBinaryFile.getOriginalEmail(
        id, 'data/emails.bin')

    data = Parser(policy=policy.default).parsestr(originalEmail)

    emailDate = data['date']
    emailTo = data['to']
    emailFrom = data['from']
    emailSubject = data['subject']
    emailBody = data.get_body(preferencelist=('plain')).get_content()
    emailAttachment = "None"
    if (data.get_payload()):
        emailAttachment = data.get_payload()[1]
    emailData = {'Date': emailDate,
                 'To': emailTo,
                 'From': emailFrom,
                 'Subject': emailSubject,
                 'Body': emailBody,
                 'Attachment': emailAttachment}
    # print(emailData)
    return render_template('displayEmail.html', emailData=emailData)


if __name__ == "__main__":
    app.run(debug=True)
