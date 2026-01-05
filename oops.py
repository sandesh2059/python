# class NumAnalyzer():
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2

    
#     def is_greater(self):
#         n1 = self.number1
#         n2 = self.number2

#         if n1 > n2:
#             return n1
#         return n2
    
# obj1 = NumAnalyzer(55, 66)
# print(f"the greatest number is : {obj1.is_greater()}")


from functools import reduce

l = [22, 33, 11, 55, 23, 32, 11, 13, 74, 1, 3]

class NumAnalyzer():
    def __init__(self):
        pass
    @staticmethod    
    def cube(a):
        return a * a * a
    def cube_of_list(self):
        return list(map(self.cube, l))
    
    @staticmethod
    def sum_of_digits(a, b):

        return a + b
    def total(self):
        return reduce(self.sum_of_digits, l)
    @staticmethod
    def greater(a):
        return a > 3
    def filter_greater_three(self):
        return list(filter(self.greater, l))
    
    def greatest(self):
        for i in l:
            if l[0] > l[1]:
                greatest = l[0]
                smallest = l[1]
            else:
                greatest = l[1]
                smallest = l[0]

            for i in l[2:]:
                if i > greatest:
                    greatest = i
                if i < smallest:
                    smallest = i
        return greatest, smallest

obj1 = NumAnalyzer()

print("the sum of number in list is: ", obj1.total())
print("the cube of number in list is: ", obj1.cube_of_list())
print("the numbers in list greater than 3 are: ",obj1.filter_greater_three())
print("the greatest and smallest in list are: ",obj1.greatest())
    

