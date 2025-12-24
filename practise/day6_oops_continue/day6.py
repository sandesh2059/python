# 🧠 Assignment 5: Bank Account System (OOP)
# Class BankAccount:
# account_holder
# balance
# Methods:
# deposit(amount)
# withdraw(amount)
# check_balance()
# Rules:
# No negative deposit
# No over-withdraw
# Menu-driven program.

class BankAccount():
    name = ['sandesh', 6000]
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    
    def check_balance(self):
        return self.balance
    

    def deposite(self, amount):
        if amount < 1:
            print("invalid amount")
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient balance")
        self.balance = self.balance - amount
        return self.balance
        
    

def menu():
    name = input("enter account holder name: ")
    balance = int(input("enter balance: "))
    account = BankAccount(name, balance)
    while True:
        print("welcome to our bank")
        print("enter 1 for checking balance")
        print("enter 2 for depositing balance")
        print("enter 3 for withdrawing balance")
        print("enter 4 for exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            print(f"your balance is ", account.check_balance())

        
menu()