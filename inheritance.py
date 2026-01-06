'''

inheritance

'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal Sound"

class Dog(Animal):
    def speak(self):
        return "Woof!!"