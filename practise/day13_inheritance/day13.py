class Account:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance
    
    def check_balance(self):
        return self.balance

class SavingAccount(Account):
    def deposit(self, amount):
        return f"{self.balance + amount}"
    
    
        