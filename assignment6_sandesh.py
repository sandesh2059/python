## ASSIGNMENT 1

# class Wallet:
#     def __init__(self, ownerName, balance = 0):
#         self.__balance = float(balance)
#         self.__ownerName = ownerName
    
#     def check_balance(self):
#         return self.__balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return self.__balance
#         else:
#             return False
    
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.balance -= amount
#             return f"{amount} is withdrawn from {self.__ownerName}'s account\nyour new balance is {self.__balance}"
#         else:
#             return f"not enough balance"

# account1 = Wallet('sandesh')
# print(f"your current balance is: {account1.check_balance()}")
# print(f"your new balance after deposit is: {account1.deposit(5000)}")
# print(f"{account1.withdraw(6000)}")








## question number 2

# class SmartBulb:

#     def __init__(self, brightness):
#         self.brightness = brightness
#         self.status = False
    
#     def check_status(self):
#         return f"the bulb's status is {self.status} and the brightness is {self.brightness}"
    
#     def turnOn(self):
#         self.status = True
#         self.brightness = 100
#         return f"the bulb's status is {self.status} and the brightness is {self.brightness}"
    
#     def turnOff(self):
#         self.status = False
#         self.brightness = 0
#         return f"the bulb's status is {self.status} and the brightness is {self.brightness}"
    
#     def dim(self, value):
#         if self.status is False:
#             return f"cannot dim a already off bulb"
#         elif self.status is True:
#             if value > 0 and value < self.brightness:
#                 self.brightness -= value
#             else:
#                 return f"cannot dim to 0 or less"
#         return f"the bulb is dimmed by {value}"
# bulb1 = SmartBulb(0)
# print(f"{bulb1.check_status()}")
# print(f"{bulb1.turnOn()}")
# print(f"{bulb1.dim(int(input("how much do you want it to dim?: ")))}")
# print(f"{bulb1.check_status()}")
# print(f"{bulb1.turnOff()}")






# # question no 3



    

