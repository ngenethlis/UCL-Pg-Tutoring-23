
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def getSender(self):
        return self.sender

    def getReceiver(self):
        return self.receiver

    def getAmount(self):
        return self.amount
