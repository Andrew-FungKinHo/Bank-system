from banksystem import BankSystem
from bankaccount import BankAccount
from transaction import Transaction


menu_options = {
    1: ['Account Creation','To open a new bank account'],
    2: ['Money Deposit','To deposit money'],
    3: ['Money Withdrawl','To withdraw money'],
    4: ['Money Transfer','To transfer cash between two users'],
    5: ['List Bank Account Balance','To list the account for the particular user'],
    6: ['Display Transaction Statement','To generate transaction statement for the particular user'],
    7: ['Exit','Exit the OSL Bank System'],
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key][0], '--', menu_options[key][1])

def login(System):
    usernameInput = input("Please type in the username for your account to login.\n")
    if usernameInput not in System.listUsernames():
        print('Username not found. Please re-enter your username')
        # or press "C" to create a new account.
        return False
    else:
        currencyInput = input("Please type in the currency for your account to login.\n")
        if currencyInput not in System.listSupportedCurrencies():
            print('Currency not found. Please re-enter your currency')
            return False
        else:
            return (usernameInput,currencyInput)
if __name__=='__main__':
    System = BankSystem()
    for currency in System.listSupportedCurrencies():
        newAccount = BankAccount('OSL_FEE',currency) 
        System.addAccount(newAccount)

    while(True):
        print("Hello customer. Which action would you like to take?")
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        # Corresponding operations

        # Create account
        if option == 1:
            usernameCreated = input('Please set a username\n')
            while True:
                currencySelected = input('Please choose from following currencies for your account.\nHKD / USD / SGD\nType the corresponding 3-character uppercase currency code.\n')
                if currencySelected not in System.listSupportedCurrencies():
                    print("Please type the corresponding 3-character uppercase currency code.\n")
                    continue
                else:
                    break
            # search if the account with exact username and currency already exist
            if usernameCreated in System.listUsernames():
                if System.findAccountByUsernameAndCurrency(usernameCreated,currencySelected):
                    print('Account already exist.')
                else:
                    newAccount = BankAccount(usernameCreated,currencySelected) 
                    # add new account to the system
                    System.addAccount(newAccount)
                    print(f'Your account with the username {usernameCreated} of currency type {currencySelected} has been created successfully.')
            else:
                newAccount = BankAccount(usernameCreated,currencySelected) 
                # add new account to the system
                System.addAccount(newAccount)
                print(f'Your account with the username {usernameCreated} of currency type {currencySelected} has been created successfully.')
        else:
            username,currency = login(System)
            userAccount = System.findAccountByUsernameAndCurrency(username,currency)
            # check whether login is successful
            if userAccount:
                print('Login success.')

                # Money Deposit
                if option == 2:
                    depositAmount = float(input(f'How much {userAccount.currency} would you like to deposit to your account?\n'))
                    userAccount.deposit(depositAmount)
                    print('Deposited successfully')

                # Money Withdrawl
                elif option == 3:
                    withdrawlAmount = float(input(f'How much {userAccount.currency} would you like to withdraw from your account?\n'))
                    if userAccount.withdraw(withdrawlAmount):
                        # if withdrawl is successful, deposit the handling fee to the OSL_FEE account
                        OSL_Account = System.findAccountByUsernameAndCurrency('OSL_FEE',userAccount.currency)
                        OSL_Account.deposit(withdrawlAmount*0.01)

                # Money Transfer
                elif option == 4:
                    transferAmount = float(input(f'How much {userAccount.currency} would you like to withdraw from your account?\n'))
                    transferTargetUsername = input('Which account would you like to transfer your funds to?\n')
                    if System.findAccountByUsernameAndCurrency(transferTargetUsername,userAccount.currency) is not None: 
                        if userAccount.transfer(transferAmount):

                            targetAccount = System.findAccountByUsernameAndCurrency(transferTargetUsername,userAccount.currency)
                            targetAccount.balance += transferAmount
                            transferTransaction = Transaction(userAccount.currency,'Transfer In',depositAmount)
                            targetAccount.transactionHistory.append(transferTransaction)

                            # if transfer is successful, deposit the handling fee to the OSL_FEE account
                            OSL_Account = System.findAccountByUsernameAndCurrency('OSL_FEE',userAccount.currency)
                            OSL_Account.deposit(transferAmount*0.01)
                    else:
                        print('Transfer Target Account not found.')

                # List Bank Account Balance
                elif option == 5:
                    userAccount.listBankBalance()

                # Display Transaction Statement
                elif option == 6:
                    allAccounts = System.findAllAccountsByUsername(username)
                    statement = System.sortOverallTransactionHistory(allAccounts)
                # Exit
                elif option == 7:
                    print('Thanks for using the OSL Bank System. Have a good day.')
                    exit()
                else:
                    print('Invalid option. Please enter a number between 1 and 4.')
            else:
                print('Unable to find account. Please retry.')