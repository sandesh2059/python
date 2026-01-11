class Employee:
    def __init__(self, name, basic_salary):
        self.__name = name
        self.__basic_salary = basic_salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__calculate_salary()

    def __calculate_salary(self):
        bonus = self.__basic_salary * 0.2
        return self.__basic_salary + bonus
class Manager(Employee):
    pass
class Developer(Employee):
    pass

emp1 = Manager("Sandesh", 50000)
emp2 = Developer("Dynamo", 40000)

print(f"Manager: {emp1.get_name()}, Salary: {emp1.get_salary()}")
print(f"Developer: {emp2.get_name()}, Salary: {emp2.get_salary()}")    
