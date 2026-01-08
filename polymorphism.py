# class Shape:
#     def area(self):
#         return "area"
    
# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         return self.length * self.breadth

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
    
#     def area(self):
#         return self.length * self.length


# def area_of_shape(enter_shape):
#     return enter_shape.area()
# shape = Square(5)
# print(area_of_shape(shape))




class Shape:
    def area(self):
        print("Area of shape is undefined")
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth


# Derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function demonstrating polymorphism
def calculate_area(shape):
    print("Area:", shape.area())

rect = Rectangle(10, 5)
circ = Circle(7)

calculate_area(rect)
calculate_area(circ)
