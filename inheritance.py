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



class Phone:

    def __init__(self, name, model, RAM):
        self.name = name
        self.model = model
        self.RAM = RAM
    

class SmartPhone(Phone):
    def __init__(self, name, model, RAM, memory):
        super().__init__(name, model, RAM)
        self.memory = memory
    
    def take_photo(self):
        return "taking photo"

p1 = SmartPhone('apple','iphone 13', 6, 512)

print(p1.name)
print(p1.model)
print(p1.RAM)
print(p1.memory)
print(p1.take_photo())