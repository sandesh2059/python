class NumAnalyzer():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    
    def is_greater(self):
        n1 = self.number1
        n2 = self.number2

        if n1 > n2:
            return n1
        return n2
    
obj1 = NumAnalyzer(55, 66)
print(f"the greatest number is : {obj1.is_greater()}")
