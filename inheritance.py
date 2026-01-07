'''

inheritance

'''


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Animal Sound"

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
    
    
    
#     def speak(self):
#         parent_sound = super().speak()
#         return f"{parent_sound} woof"

# d = Dog('tommy', 'husky')
# print(d.name)
# print(d.breed)
# print(d.speak())



# class Phone:

#     def __init__(self, name, model, RAM):
#         self.name = name
#         self.model = model
#         self.RAM = RAM
    
#     def calling(self):
#         return "ONLY audio call supported"
    

# class SmartPhone(Phone):
#     def __init__(self, name, model, RAM, memory):
#         super().__init__(name, model, RAM)
#         self.memory = memory
    
#     def take_photo(self):
#         return "taking photo"
    
#     def calling(self):
#         return "BOTH audio and video call supported"

# p1 = SmartPhone('apple','iphone 13', 6, 512)

# print(p1.name)
# print(p1.model)
# print(p1.RAM)
# print(p1.memory)
# print(p1.take_photo())
# print(p1.calling())




class Department:
    def __init__(self, department):
        self.department = department
    
    
        


class Employee:
    def __init__(self, employee_name):

        self.employee_name = employee_name


class FunctionalDesignation:
    def __init__(self, position):
        self.position = position
        


class Internship(Department, Employee, FunctionalDesignation):
    def __init__(self, department, employee_name, position,intern_name, internship_duration):
        Department.__init__(self, department)
        Employee.__init__(self, employee_name)
        FunctionalDesignation.__init__(self, position)
        self.internship_duration = internship_duration
        self.intern_name = intern_name
    

    
    
    
        
            

    
    
class InternshipInfoContainer:

    def __init__(self, marketing = None, frontend = None, backend = None):
        self.marketing = []
        self.frontend = []
        self.backend = []
    def total(self):
        

    
    

        for intern in intern_list:
            if intern.department == 'Marketing':
                self.marketing.append(intern.intern_name)
            elif intern.department == 'Frontend':
                self.frontend.append(intern.intern_name)
            elif intern.department == 'Backend':
                self.backend.append(intern.intern_name)
        return self.marketing , self.frontend, self.backend
            
        
        

intern1 = Internship('Marketing', 'Alice', 'Manager', 'John', 3)
intern2 = Internship('Frontend', 'Bob', 'Team Lead', 'Emma', 6)
intern3 = Internship('Backend', 'Charlie', 'Senior Dev', 'Liam', 4)
intern4 = Internship('Backend', 'David', 'Senior Dev', 'Olivia', 5)
intern5 = Internship('Backend', 'Eve', 'Team Lead', 'Noah', 5)
intern6 = Internship('Frontend', 'Frank', 'Developer', 'Ava', 3)
intern7 = Internship('Frontend', 'Grace', 'Developer', 'Sophia', 4)
intern8 = Internship('Frontend', 'Hannah', 'Team Lead', 'Mason', 5)
intern9 = Internship('Marketing', 'Ian', 'Manager', 'Isabella', 3)
intern10 = Internship('Marketing', 'Jack', 'Executive', 'Ethan', 5)
intern_list = [intern1, intern2, intern3, intern4, intern5, intern6, intern7, intern8, intern9, intern10]

info = InternshipInfoContainer(intern_list)
print(info.total())





