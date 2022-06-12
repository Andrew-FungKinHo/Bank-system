from bankaccount import BankAccount
class BankSystem():
    def __init__(self):
        self.accounts = []
        # self.defaultAccount = BankAccount('OSL_FEE','HKD')
        self.currenciesSupported = ['HKD','USD','SGD']

    def listUsernames(self):
        return [account.username for account in self.accounts]

    def listSupportedCurrencies(self):
        return [currency for currency in self.currenciesSupported]

    def addAccount(self,account):
        self.accounts.append(account)

    def findAccountByUsernameAndCurrency(self,username,currency):
        for account in self.accounts:
            if username == account.username:
                if currency == account.currency:
                    return account

    def findAllAccountsByUsername(self,username):
        allAccountsForUser = []
        for account in self.accounts:
            if username == account.username:
                allAccountsForUser.append(account)
        return allAccountsForUser
    
    def sortOverallTransactionHistory(self,accountList):
        overallStatement = []
        for account in accountList:
            overallStatement.extend(account.transactionHistory)

        # sort the transactionHistory of all accounts
        overallStatement = sorted(overallStatement, key=lambda x: x.date)
        # print statement
        print(f"Client Name\t\t\t{accountList[0].username}")
        print("Date\t\t\t\tCurrency\tOperation\t\tAmount")
        for transaction in overallStatement:
            print(f"{transaction.date}\t{transaction.currency}\t\t{transaction.operation}\t\t{transaction.amount}")
        return overallStatement
        