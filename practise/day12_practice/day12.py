# 🧩 LEVEL 1: Core Python (Logic + Confidence)
# Task 1: Number Utility

# Create functions to:

# Reverse a number

# Check palindrome

# Count digits

# Sum of digits

# 👉 Rules

# No input inside logic functions

# Use return

# One menu function handles input/output

class NumberAnalyzer():

    def __init__(self, n):
        self.number = n

    def reverse(self):
        rev = 0
        n = self.number
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        return rev   

    def palindrome(self):
        if self.number == self.reverse():
            return True
        return False
    def count_digits(self):
        count = 0
        n = self.number
        while n > 0:
            
            count += 1
            n //= 10
            
        return count
    def sum_of_digits(self):
        total = 0
        n = self.number
        while n > 0:
            
            total += n % 10
            n //= 10
        return total
num1 = NumberAnalyzer(334433)
print(f"the reverse of {num1.number} is {num1.reverse()}")
print(f"palindrome: {num1.palindrome()}")
print(f"the total number of digits in {num1.number} is {num1.count_digits()}")
print(f"the sum of all digits in {num1.number} is {num1.sum_of_digits()}")
            

        