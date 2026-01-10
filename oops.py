# # class NumAnalyzer():
# #     def __init__(self, number1, number2):
# #         self.number1 = number1
# #         self.number2 = number2

    
# #     def is_greater(self):
# #         n1 = self.number1
# #         n2 = self.number2

# #         if n1 > n2:
# #             return n1
# #         return n2
    
# # obj1 = NumAnalyzer(55, 66)
# # print(f"the greatest number is : {obj1.is_greater()}")


# from functools import reduce

# l = [22, 33, 11, 55, 23, 32, 11, 13, 74, 1, 3]

# class NumAnalyzer():
#     def __init__(self):
#         pass
#     @staticmethod    
#     def cube(a):
#         return a * a * a
#     def cube_of_list(self):
#         return list(map(self.cube, l))
    
#     @staticmethod
#     def sum_of_digits(a, b):

#         return a + b
#     def total(self):
#         return reduce(self.sum_of_digits, l)
#     @staticmethod
#     def greater(a):
#         return a > 3
#     def filter_greater_three(self):
#         return list(filter(self.greater, l))
    
#     def greatest(self):
#         for i in l:
#             if l[0] > l[1]:
#                 greatest = l[0]
#                 smallest = l[1]
#             else:
#                 greatest = l[1]
#                 smallest = l[0]

#             for i in l[2:]:
#                 if i > greatest:
#                     greatest = i
#                 if i < smallest:
#                     smallest = i
#         return greatest, smallest

# obj1 = NumAnalyzer()

# print("the sum of number in list is: ", obj1.total())
# print("the cube of number in list is: ", obj1.cube_of_list())
# print("the numbers in list greater than 3 are: ",obj1.filter_greater_three())
# print("the greatest and smallest in list are: ",obj1.greatest())
    



# class BankAccount():
#     def __init__(self, balance, number, history=[]):
#         self.balance = balance
#         self.number = number
#         self.history = history
     
        
#     def check_balance(self):
#         return self.balance
    
#     def deposite(self, amount):
#         self.balance += amount
#         self.history.append(f"deposite: {amount}")
        


#         return self.balance
    
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#             self.history.append(f"withdraw: {amount}")
#             return self.balance
#         return False
    
#     # def transaction_history(self, transferfrom):
#     #     if transferfrom.deposite()
        


    
#     # def fund_transfer(self, amount):
#     #     if amount < self.balance1:
#     #         self.balance1 -= amount
#     #         self.balance2 += amount
            
#     #         return self.balance2
#     #     return False

#     def fund_transfer(self, transferto, amount):
#         print(f"the current balance is: {self.balance}")
#         if amount <= self.balance:
#             self.balance -= amount
#             transferto.balance += amount
#             self.history.append(f'The transfer amount: {amount}')
#             return f"the new balance of account 1 is: {self.balance} , the fund transfered is {amount} and the new balance of account 2 is: {transferto.balance}"
#         else:
#             return f"not enough amount"




# transferfrom = BankAccount(5000, 23081019)
# transferTo = BankAccount(1000, 19876232)
# print("transfer from ", transferfrom.fund_transfer(transferTo, 1000))

# print("your balance is: ", transferfrom.check_balance())
# print("your balance after deposite is: ", transferfrom.deposite(4000))
# print("your bakance after withdrawl is: ", transferfrom.withdraw(1000))


# print(f"history : {transferfrom.history}")
# # print(f"new balance in account number 2 after fund transfer from number 1 is: ", obj1.fund_transfer(1000))





from abc import ABC, abstractmethod

# =========================
# ABSTRACTION (Abstract Class)
# =========================
class Employee(ABC):

    company = "TechSoft Pvt. Ltd."   # Class variable (Encapsulation)

    def __init__(self, name, salary):
        self.__name = name          # Private variable (Encapsulation)
        self.__salary = salary      # Private variable

    # Getter method (Encapsulation)
    def get_details(self):
        return self.__name, self.__salary

    # Abstract method (Abstraction)
    @abstractmethod
    def calculate_bonus(self):
        pass

    # Class method
    @classmethod
    def show_company(cls):
        print("Company:", cls.company)

    # Static method
    @staticmethod
    def is_high_salary(salary):
        return salary >= 50000
# =========================
# INHERITANCE + POLYMORPHISM
# =========================
class Manager(Employee):

    def calculate_bonus(self):      # Method overriding (Polymorphism)
        name, salary = self.get_details()
        return salary * 0.20

class Developer(Employee):

    def calculate_bonus(self):      # Method overriding (Polymorphism)
        name, salary = self.get_details()
        return salary * 0.10

# =========================
# POLYMORPHIC FUNCTION
# =========================
def show_employee_info(emp):
    name, salary = emp.get_details()
    print("\nName:", name)
    print("Salary:", salary)
    print("Bonus:", emp.calculate_bonus())   # Polymorphism

    if Employee.is_high_salary(salary):
        print("Salary Level: High")
    else:
        print("Salary Level: Normal")

















