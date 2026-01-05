class Wallet:
    def __init__(self, ownerName, balance = 0):
        self.__balance = float(balance)
        self.__ownerName = ownerName
    
    def check_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.balance -= amount
            return f"{amount} is withdrawn from {self.__ownerName}'s account\nyour new balance is {self.__balance}"
        else:
            return f"not enough balance"
    
    

