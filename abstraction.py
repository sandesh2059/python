# # from abc import ABC, abstractmethod

# # class Shape(ABC):

# #     @abstractmethod
# #     def area(self):
# #         pass

# # class Circle(Shape):

# #     def area(self, radius):
# #         return 3.14 * radius * radius
# #     def perimeter(self, radius):
# #         return 2 * 3.14 * radius

# # def area_of(shape):
# #     print(f"area is {shape.area(4)}")

# # def perimeter_of(shape):
# #     print(f"perimeter is {shape.perimeter(4)}")


# # circ = Circle()

# # area_of(circ)
# # perimeter_of(circ)



# # coffeeMachine

# from abc import ABC, abstractmethod

# class CoffeeMachine(ABC):

#     @abstractmethod
#     def make_coffee(self):
#         pass


# class LatteMachine(CoffeeMachine):

#     def make_coffee(self):
#         return f"using 100 gram of coffee beans to make latte coffee"

# class MochaMachine(CoffeeMachine):

#     def make_coffee(self):
#         return f"using 50 gram of mocha coffee bean to make mocha coffee"

# def machine(coffee):
#     print(f" {coffee.make_coffee()}")

# mocha = MochaMachine()
# latte = LatteMachine()

# machine(mocha)
# machine(latte)

  


# using encapsulation achieve abstraction ... note: avoid polymorphism



from abc import ABC, abstractmethod

# ------------------------------
# Abstract Class
# ------------------------------
class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass
class SBI(Bank):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"SBI: Deposited Rs.{amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"SBI: Withdrawn Rs.{amount}")
        else:
            print("SBI: Insufficient balance")

    def check_balance(self):
        print(f"SBI: Current Balance Rs.{self.balance}")

class Nabil(Bank):
    def __init__(self):
        self.balance = 0
