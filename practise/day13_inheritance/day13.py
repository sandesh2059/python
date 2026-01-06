class Account:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance
    
    def check_balance(self):
        return self.balance

class SavingAccount(Account):
    def deposit(self, amount):
        return f"{self.balance + amount}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn from {self.acc_number}"
        else:
            return "not enough balance"

acc1 = SavingAccount(23081019, 40000)
print(f"deposit: {acc1.deposit(1000)}")

        