from transaction import Transaction


class BankAccount():
    def __init__(self,username,currency):
        self.username = username
        self.currency = currency
        self.balance = 0.0
        self.transactionHistory = []

    # Display transaction statement: To generate transaction statement for the particular user
    def printTransactionStatement(self):
        print(f"Client Name\t{self.username}")
        print("Date\tCurrency\tOperation\tAmount")

    # List bank account balance: To list the account for the particular user
    def printBalance(self):
        print(f'Your account has the balance of: {self.balance}')
    
    # # Money transfer: To transfer cash between two users
    # def transfer(self,recipientUsername,transferAmount):
    #     if recipientUsername in 

    # Money withdrawl: To withdraw money
    def withdraw(self,withdrawlAmount):
        # not enough funds for the withdrawl amount
        if self.balance < (withdrawlAmount * 1.01):
            print('Money withdrawl was unsuccessful.')
            
        else:
            # implement more than 5 withdrawals check here
            self.balance -= withdrawlAmount
            withdrawlTransaction = Transaction(self.currency,'Withdrawl',withdrawlAmount)
            self.transactionHistory.append(withdrawlTransaction)

            self.balance -= withdrawlAmount * 0.01
            withdrawlFeeTransaction = Transaction(self.currency,'Withdrawl FEE',withdrawlAmount * 0.01)
            self.transactionHistory.append(withdrawlFeeTransaction)

            # add money to OSL_FEE account?

    # Money deposit: To deposit money
    def deposit(self,depositAmount):
        self.balance += depositAmount
        depositTransaction = Transaction(self.currency,'Deposit',depositAmount)
        self.transactionHistory.append(depositTransaction)
        print('Deposited successfully')

    # Account creation: To open a new bank account
