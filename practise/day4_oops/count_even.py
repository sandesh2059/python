# Write a function count_even_digits(n) that returns how many even digits are in a number.

class program:

    def __init__(self, n):
        self.n = n
    

    def count_even(self):
        n = self.n
        last_digit = 0
        count = 0
        while n > 0:
            last_digit = n % 10
            if last_digit % 2 == 0:
                count += 1
            n //= 10
        return count

    def show_count_even(self):
        print("the total number of even digits are: ", self.count_even())

num = int(input("enter a number: "))
obj1 = program(num)
obj1.show_count_even()
            