class Log:
    id = 0
    date = ""
    time = ""
    toAddress = ""
    fromAddress = ""
    subject = ""
    action = ""

    def __init__(self, id, date, time, toAddress, fromAddress, subject, action ):
        self.id = id
        self.date = date
        self.time = time
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.subject = subject
        self.action = action