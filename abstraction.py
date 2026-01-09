# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):

#     def area(self, radius):
#         return 3.14 * radius * radius
#     def perimeter(self, radius):
#         return 2 * 3.14 * radius

# def area_of(shape):
#     print(f"area is {shape.area(4)}")

# def perimeter_of(shape):
#     print(f"perimeter is {shape.perimeter(4)}")


# circ = Circle()

# area_of(circ)
# perimeter_of(circ)



# coffeeMachine

from abc import ABC, abstractmethod

class CoffeeMachine(ABC):

    @abstractmethod
    def make_coffee(self):
        pass


class LatteMachine(CoffeeMachine):

    def make_coffee(self):
        return f"using 100 gram of coffee beans to make latte coffee"

class MochaMachine(CoffeeMachine):

    def make_coffee(self):
        return f"using 50 gram of mocha coffee bean to make mocha coffee"

def machine(coffee):
    print(f" {coffee.make_coffee()}")

mocha = MochaMachine()
latte = LatteMachine()

machine(mocha)
machine(latte)


























