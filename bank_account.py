import random


class BankAccount:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.account_number = random.randint(10000, 99999)
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Deposited ${amount:,.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:,.2f}.")

    def display_account_info(self):
        print(f"\nName: {self.customer_name}")
        print(f"Account #: {self.account_number}")
        print(f"Balance: ${self.balance:,.2f}")