class number_analyzer():

    def __init__(self, n):
        self.n = n
    
    def reverse(self):
        rev = 0
        while self.n > 0:
            rev = rev * 10 + (self.n % 10)
            self.n //= 10
            return rev
    
    def is_palindrome(self):
        return self.is_palindrome == self.reverse
    
    def total_digits(self):
        count = 0
        while self.n > 0:
            count += 1
            self.n //= 10
            return count

    def sum_of_digits(self):
        total = 0
        while self.n > 0:
            total += self.n % 10
            self.n //= 10
        return total 

    
    





n1 = number_analyzer(23412)