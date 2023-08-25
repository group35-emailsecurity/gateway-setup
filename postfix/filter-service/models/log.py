class Log:
    id = 0
    date = ""
    time = ""
    toAddress = ""
    fromAddress = ""
    subject = ""
    message = ""
    type = ""
    action = ""

    def __init__(self, id, date, time, toAddress, fromAddress, subject, message, type, action ):
        self.id = id
        self.date = date
        self.time = time
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.subject = subject
        self.message = message
        self.type = type
        self.action = action