import datetime
from transaction import Transaction


class BankAccount():
    def __init__(self,username,currency):
        self.username = username
        self.currency = currency
        self.balance = 0.0
        self.transactionHistory = []

    # Money deposit: To deposit money
    def deposit(self,depositAmount):
        self.balance += depositAmount
        depositTransaction = Transaction(self.currency,'Deposit',depositAmount)
        self.transactionHistory.append(depositTransaction)

    # Money withdrawl: To withdraw money
    def withdraw(self,withdrawlAmount):
        # not enough funds for the withdrawl amount
        if self.balance < (withdrawlAmount * 1.01):
            print('Money withdrawl was unsuccessful due to insufficient funds.')
            return False
            
        else:
            # check the number of transactions (withdrawl) within 5 minutes
            transactionsWithinFiveMinutes = []
            for transaction in self.transactionHistory:
                if (datetime.datetime.now() - transaction.date <= datetime.timedelta(0,5*60)) and transaction.operation == 'Withdrawl':
                    transactionsWithinFiveMinutes.append(transaction)

            if len(transactionsWithinFiveMinutes) > 4:
                print('Money withdrawl was unsuccessful as you have surpassed the 5-minute threshold limit of 5 withdrawls. Please try again later.')
                return False
            else:
                self.balance -= withdrawlAmount
                withdrawlTransaction = Transaction(self.currency,'Withdrawl',withdrawlAmount)
                self.transactionHistory.append(withdrawlTransaction)

                self.balance -= withdrawlAmount * 0.01
                withdrawlFeeTransaction = Transaction(self.currency,'Withdrawl FEE',withdrawlAmount * 0.01)
                self.transactionHistory.append(withdrawlFeeTransaction)
                print('Withdrew successfully')
                return True

    # Money transfer: To transfer cash between two users
    def transfer(self,transferAmount):
        # not enough funds for the withdrawl amount
        if self.balance < (transferAmount * 1.01):
            print('Money Transfer was unsuccessful due to insufficient funds.')
            return False
            
        else:
            # implement more than 5 withdrawals check here
            self.balance -= transferAmount
            transferTransaction = Transaction(self.currency,'Transfer Out',transferAmount)
            self.transactionHistory.append(transferTransaction)

            self.balance -= transferAmount * 0.01
            transferFeeTransaction = Transaction(self.currency,'Transfer Out FEE',transferAmount * 0.01)
            self.transactionHistory.append(transferFeeTransaction)

            print('Transferred successfully')

            return True


    # List bank account balance: To list the account for the particular user
    def listBankBalance(self):
        print(f'Your account has the balance of: {self.balance}')