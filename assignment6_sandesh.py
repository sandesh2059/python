class Wallet:
    def __init__(self, ownerName, balance = 0):
        self.__balance = float(balance)
        self.__ownerName = ownerName
    
    def check_balance(self):
        return self.__balance
    
    

