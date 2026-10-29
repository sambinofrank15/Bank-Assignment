from bank_account import BankAccount
#importing functions from bank_account.py file to mainBank.py file

def main():
    print("Welcome to the Bank of Sam!")

    customer_name = input("Please enter your name: ")
    account = BankAccount(customer_name) #Define both variables customer_name and account 
    #to create a new instance of the BankAccount class.

    while True: #show options to the user until they choose to quit
        print("\nPlease choose an option:")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. View account information")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(
                    input("How much would you like to deposit? ")
                )

                account.deposit(amount)

            except ValueError:
                print("Please enter a valid number.") #Validate user input

        elif choice == "2":
            try:
                amount = float(
                    input("How much would you like to withdraw? ")
                )

                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid number.") #Validate user input

        elif choice == "3":
            account.display_account_info()

        elif choice == "4":
            print("Thank you for using the Bank of Sam!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()