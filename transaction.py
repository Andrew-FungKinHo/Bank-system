import datetime
class Transaction():
    def __init__(self,currency,operation,amount):
        self.date = datetime.datetime.now()
        self.currency = currency
        self.operation = operation
        self.amount = amount