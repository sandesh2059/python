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
#         self.__brightness = brightness
#         self.__status = False
    
#     def check_status(self):
#         return f"the bulb's status is {self.__status} and the brightness is {self.__brightness}"
    
#     def turnOn(self):
#         self.__status = True
#         self.__brightness = 100
#         return f"the bulb's status is {self.__status} and the brightness is {self.__brightness}"
    
#     def turnOff(self):
#         self.__status = False
#         self.__brightness = 0
#         return f"the bulb's status is {self.__status} and the brightness is {self.__brightness}"
    
#     def dim(self, value):
#         if self.__status is False:
#             return f"cannot dim a already off bulb"
#         elif self.__status is True:
#             if value > 0 and value < self.__brightness:
#                 self.__brightness -= value
#             else:
#                 return f"cannot dim to 0 or less"
#         return f"the bulb is dimmed by {value}"
# bulb1 = SmartBulb(0)
# print(f"{bulb1.check_status()}")
# print(f"{bulb1.turnOn()}")
# print(f"{bulb1.dim(int(input("how much do you want it to dim?: ")))}")
# print(f"{bulb1.check_status()}")
# print(f"{bulb1.turnOff()}")






# # # question no 3
class Car:

    def __init__(self, modelName, fuelLevel):
        self.__modelName = modelName
        self.setFuel_level(fuelLevel)
    
    def setFuel_level(self, fuelLevel):
        if fuelLevel >= 0 and fuelLevel <= 100:
            self.__fuelLevel = fuelLevel
        else:
            print("invalid fuel level")
    
    def check_fuelLevel(self):
        return f"the fuel level is: {self.__fuelLevel}"
    
    def drive(self):
        if self.__fuelLevel <= 0:
            return f"cannot drive as fuel is finished"
        else:
            self.__fuelLevel -= 10
            return f"fuel level reduced by 10 after driving"

    def refeul(self, amount):
        if self.__fuelLevel == 100:
            return f"cannot reful as fuel level is max"
        elif amount + self.__fuelLevel > 100:
            self.__fuelLevel = 100
            return f"tank is overflow, setting fuel level to 100"
        else:
            self.__fuelLevel += amount
            return f"the fuel level is: {self.__fuelLevel}"


car1 = Car('suzuki', 50)
print(f"{car1.check_fuelLevel()}")
print(f"{car1.drive()}")
print(f"{car1.check_fuelLevel()}")
print(f"{car1.refeul(int(input("enter the amount to refuel: ")))}")


    



    




    

