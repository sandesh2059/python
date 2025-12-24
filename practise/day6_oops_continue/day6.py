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
    account_holder = 'sandesh'
    balance = 6000
    def __init__(self, account_holder, balance, amount):
        self.account_holder = account_holder
        self.balance = balance
        self.amount = amount

    
    def check_balance(self):
        return self.balance
    

    def deposite(self):
        amount = self.amount
        balance = self.balance
        amount = int(input("Enter amount to deposite: "))
        balance = balance + amount
        return balance
    
    def withdraw(self):
        self.amount = int(input("Enter amount to withdraw: "))
        self.balance = self.balance - self.amount
        print(f"({self.amount} was withdrawn you new balance is {check_balance()})")