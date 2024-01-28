# Assume that this is a unit used from the main program
from transaction import Transaction


class Client:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.balance = 0
        self.transactions: [Transaction]
        self.transactions = []

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def getBalance(self):
        return self.balance

    def getTransactions(self):
        return self.transactions

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        self.phone = phone

    def setBalance(self, balance):
        self.balance = balance

    def setTransactions(self, transactions):
        self.transactions = transactions

    def addTransaction(self, transaction):
        self.transactions.append(transaction)
        self.balance += transaction.getAmount()

    def __str__(self):
        return "Name: " + self.name + "\nAddress: " + self.address + "\nPhone: " + self.phone + "\nBalance: " + str(
            self.balance) + "\nTransactions: " + str(self.transactions)
