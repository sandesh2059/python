# Assignment 1: Smart Calculator (Function Based)

# Create functions for:

# add(a, b)

# subtract(a, b)

# multiply(a, b)

# divide(a, b)

# Create a menu-driven program that:

# Takes user input

# Calls the correct function

# Uses return properly (NO printing inside logic functions)



def add(a , b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

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
            print(f"The sum of {a} and {b} is: ", add(a , b) )
        
        elif choice == 2:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            print(f"The difference between {a} and {b} is: ", subtract(a , b))

        elif choice == 3:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            result = multiply(a , b)
            print(f"The product of {a} and {b} is: ", multiply(a , b))

        elif choice == 4:
            a = int(input("Enter the first value: "))
            b = int(input("Enter the second value: "))
            result = divide(a , b)
            print(f"{a} divided by {b} is: ", divide(a , b))
        
        elif choice == 5:
            print("exiting")
            break

        else:
            print("invalid choice")
menu()

            

