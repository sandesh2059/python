from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self, radius):
        return 3.14 * radius * radius
    def perimeter(self, radius):
        return 2 * 3.14 * radius

def area_of(shape):
    print(f"area is {shape.area(4)}")

def perimeter_of(shape):
    print(f"perimeter is {shape.perimeter(4)}")


circ = Circle()

area_of(circ)
perimeter_of(circ)

