class Email:
    id = 0
    toAddress = ""
    fromAddress = ""
    subject = ""
    body = ""

    def __init__(self, id, toAddress, fromAddress, subject, body ):
        self.id = id
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.subject = subject
        self.body = body