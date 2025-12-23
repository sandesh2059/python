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

        # if choice == 1:
        #     a = int(input("Enter the first value: "))
        #     b = int(input("Enter the second value: "))

