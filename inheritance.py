'''

inheritance

'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal Sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return "woof"

d = Dog('tommy', 'husky')
print(d.name)
print(d.breed)
print(d.speak())
