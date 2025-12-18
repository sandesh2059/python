# # Task 1: The "FizzBuzz" Classic (Pattern Logic)
# # Goal: Practice multiples and modulo operations using loops and nested conditionals.
# # The Problem:Write a program that prints numbers from 1 to 50.
# # If the number is a multiple of 3, print "Fizz" instead of the number.
# # If it is a multiple of 5, print "Buzz".
# # If it is a multiple of both 3 and 5, print "FizzBuzz".
# # Otherwise, just print the number.


# for i in range(1, 51):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")        
#     else:
#         print(i)








# # # Task 2: Find the Maximum and Minimum (Array Traversal)
# # Goal: Understand how to keep track of state variables while looping through a list.
# # The Problem:Given a list of numbers (e.g., [23, 45, 12, 56, 89, 3, 44]), 
# # write a loop to find the largest and smallest numbers in the list without using built-in functions like max() or min().
# #  Remarks: Please dont use the same method that we use in class.


# marks = [23, 45, 12, 56, 89, 3, 44]
# if marks[0] > marks[1]:
        
#         smallest = marks[1]
#         largest = marks[0]

# else:

#         smallest = marks[0]
#         largest = marks[1]

# for i in range(2, len(marks)):
#         if marks[i] < smallest:
#             smallest = marks[i]
#         elif marks[i] > largest:
#             largest = marks[i]
   
# print(smallest)
# print(largest)







# # Task 4: Prime Number Checker (Efficiency Logic)
# # Goal: Understand the "break" statement and boolean flags.
# # The Problem:Ask the user for a number and determine if it is a Prime Number.
# # A prime number is only divisible by 1 and itself.
# # Logic: Use a for loop to check if any number from 2 up to the square root of the input divides it perfectly.
# #    Use an if/else block to print the final result.


# a = int(input("Enter a number: "))
# if a <= 1:
#         print(f"{a} is not a prime")
# else:
     
#     for i in range(2, int(a ** 0.5) + 1):
#         if a % i == 0:
#             print(f"{a} is not a prime number")
#             break
#     else:  
#         print(f"{a} is a prime")









# Task 5: The Fibonacci Sequence (Algorithmic Thinking)
# Goal: Learn how to update multiple variables simultaneously within a loop.
# The Problem:Write a program to generate the first N terms of the Fibonacci sequence.
# The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, ... (Each number is the sum of the two preceding ones).
# Use a loop to calculate the next term and update your "previous" and "current" variables accordingly.



# a = 0
# b = 1
# c = a + b
# N = int(input("Enter a Nth term of fibinacci series: "))

# if N <= 1:
#     print("Please choose a number higher than 1")
# else:
#     print(a, end=" ")
#     print(b, end=" ")

# for i in range(2, N):
#     c = a + b
#     a = b 
#     b = c
#     print(c, end =" ")






# # Task 3: Reverse a Number (Mathematical Loop)
# # Goal: Practice while loops and using the modulo % and floor division // operators.
# # The Problem:Take an integer input from the user (e.g., 1234) and print it in reverse order (e.g., 4321).
# # Constraint: Do not convert the number to a string. Use mathematical operations inside a while loop 
# # to extract digits one by one.


# num = int(input("Enter a number: "))
# reverse = 0
# while num != 0:
#     last_digit = num % 10
#     reverse = reverse * 10 + last_digit
#     num //= 10
# print(reverse)