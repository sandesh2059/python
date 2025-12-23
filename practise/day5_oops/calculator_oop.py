class calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
    
        return self.a + self.b

    def subtract(self):
        
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        
        if self.b == 0:
            return "cannot divide by zero"
        return self.a / self.b

def menu():
    while True:
        print("-----calculator-----")
        print("1. perform addition")
        print("2. perform subtraction")
        print("3. perform multiplication")
        print("4. perform division")
        print("5. exit")

        choice = int(input("enter your choice: "))

        if choice == 1:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            
            obj1 = calculator(a , b)
            obj1.add()
            result = obj1.add()
            print(f"the sum of {a} and {b} is: {result}", )
        
        elif choice == 2:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            obj1 = calculator(a , b)
            obj1.subtract()
            result = obj1.subtract()
            print(f"the difference of {a} and {b} is: {result}")

        elif choice == 3:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            obj1 = calculator(a , b)
            obj1.multiply()
            result = obj1.multiply()
            print(f"the multiplication of {a} and {b} is: {result}")

        elif choice == 4:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            obj1 = calculator(a , b)
            obj1.divide()
            result = obj1.divide()
            print(f"the division of {a} and {b} is: ", result)
        
        elif choice == 5:
            print("exiting")
            break

        else:
            print("invalid choice")
menu()

            


        



    