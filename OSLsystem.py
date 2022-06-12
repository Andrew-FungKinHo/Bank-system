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

    def findAccountByUsername(self,username):
        for account in self.accounts:
            if username == account.username:
                return account