import sql_manager
import re
import hashlib
import getpass


def main_menu():
    print(
        "Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            isSubstring = password in username
            enoughSymbol = len(password) > 8
            containNumber = any(char.isdigit() for char in password)
            containSpecSymbol = re.match('^[a-zA-Z0-9-_]*$', password)
            containCapitalLetter = any(map(str.isupper, password))
            if containSpecSymbol == None:
                containSpecSymbol = True
            else:
                containSpecSymbol = False

            if(not isSubstring and enoughSymbol and containNumber and containSpecSymbol and containCapitalLetter):

                password_bytes = password.encode('utf-8')
                hash_object = hashlib.sha1(password_bytes)
                hex_dig = hash_object.hexdigest()

                sql_manager.register(username, hex_dig)
                print("Registration Successfull")

            else:
                print("Your password must be: ")
                print("More then 8 symbols")
                print(
                    "Must have capital letters, and numbers and a special symbol")
                print("Username is not in the password (as a substring)")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            password_bytes = password.encode('utf-8')
            hash_object = hashlib.sha1(password_bytes)
            hex_dig = hash_object.hexdigest()

            logged_user = sql_manager.login(username, hex_dig)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("display - for display current balance")
            print("deposit - for deposit money")
            print("withdraw - for withdraw money")
        elif command == 'deposit':
            money = input("Enter amount: ")
            sql_manager.deposit_money(money, logged_user)
            print("Transaction successful!")
        elif command == 'display':
            sql_manager.display_money(logged_user)
        elif command == 'withdraw':
            money = input("Enter amount: ")
            sql_manager.withdraw_money(logged_user, money)



def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
