class Shape:
    def area(self):
        return "area"
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length


def area_of_shape(Shape):
    return Shape.area()
shape = Square(5)
print(area_of_shape(shape))
