class number_analyzer():

    def __init__(self, n):
        self.n = n
    
    def reverse(self):
        n = self.n
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        return rev
    
    def is_palindrome(self):
        return self.n == self.reverse()
    
    def total_digits(self):
        n = self.n
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    def sum_of_digits(self):
        n = self.n
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total 
    


    def analyze(self):
        print("-----number analysis------")
        print("the number is: ", self.n)
        print("the reverse is: ", self.reverse())
        print("Palindrome: ", "YES" if self.is_palindrome() else "NO")
        print("the total digits are: ", self.total_digits())
        print("the sum of all the digits is: ", self.sum_of_digits())


def menu():
    while True:
        print("choose the number")
        print("1. perform number analysis")
        print("2. exit")

        choice = input("Enter a number: ")

        if choice == '1':
            num = int(input("enter your number to perform analysis: "))
            obj1 = number_analyzer(num)
            obj1.analyze()
        

        elif choice == '2':
            print("Exiting")
            break

        else:
            print("invalid choice")

menu()

    
    




