class Log:
    id = 0
    date = ""
    time = ""
    toAddress = ""
    fromAddress = ""
    subject = ""
    message = ""
    action = ""

    def __init__(self, id, date, time, toAddress, fromAddress, subject, message, action ):
        self.id = id
        self.date = date
        self.time = time
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.subject = subject
        self.message = message
        self.action = action