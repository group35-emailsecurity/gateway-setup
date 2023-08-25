from flask import Flask, render_template, url_for
import json
import os
import pickle
import writeEmailObjectsToBinaryFile
import writeLogObjectsToBinaryFile
from models.email import Email
from models.log import Log

app = Flask(__name__)
       
@app.route('/')
def index():
    pieChartData = {'Task' : 'Total emails', 'Allowed' : 234, 'Blocked' : 153, 'Quarantine' : 86}
    barChartData = {'Task' : 'Threats found', 'Virus' : 57, 'Spam' : 56, 'Phishing' : 40}
    #print(data)
    
    return render_template('index.html', pieChartData = pieChartData, barChartData = barChartData)

@app.route('/emails')
def emails():
    headings = ("ID","To","From","Subject","Body")
    emailData = writeEmailObjectsToBinaryFile.readFromBinaryFileToEmailList('data/emails.bin')
    return render_template('emails.html',emailData = emailData,headings = headings)

@app.route('/logs')
def logs():
    headings = ("ID","Date","Time","To","From","Subject", "Message", "Type", "Action")
    logData = writeLogObjectsToBinaryFile.readFromBinaryFileToLogList('data/logs.bin')
    return render_template('logs.html', logData = logData, headings = headings)

@app.route('/login')
def login():
    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)
