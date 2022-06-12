from OSLsystem import BankSystem
from bankaccount import BankAccount


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
        print('Login success.')
        return usernameInput
if __name__=='__main__':
    System = BankSystem()

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
                if System.findAccountByUsername(usernameCreated).currency == currencySelected:
                    print('Account already exist.')
            else:
                newAccount = BankAccount(usernameCreated,currencySelected) 
                # add new account to the system
                System.addAccount(newAccount)
        else:
            username = login(System)
            userAccount = System.findAccountByUsername(username)
            # Money Deposit
            if option == 2:
                depositAmount = float(input(f'How much {userAccount.currency} would you like to deposit to your account?\n'))
                userAccount.deposit(depositAmount)
            # Money Withdrawl
            elif option == 3:
                withdrawlAmount = float(input(f'How much {userAccount.currency} would you like to withdraw from your account?\n'))
                userAccount.withdraw(withdrawlAmount)
            # Money Transfer
            elif option == 4:
                pass
            # List Bank Account Balance
            elif option == 5:
                pass
            # Display Transaction Statement
            elif option == 6:
                pass
            # Exit
            elif option == 7:
                print('Thanks for using the OSL Bank System. Have a good day.')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')