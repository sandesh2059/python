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
    


    def analyze(self):
        print("-----number analysis------")
        print("the number is: ", self.n)
        print("the reverse is: ", self.reverse())
        print("Palindrome: ", "YES" if self.is_palindrome() else "NO")
        print("the total digits are: ", self.total_digits())
        print("the sum of all the digits is: ", self.sum_of_digits())

    
    





n1 = number_analyzer(23412)