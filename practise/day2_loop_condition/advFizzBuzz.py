# Task 1: Advanced FizzBuzz Variations
# Goal: Master nested conditionals and modulo logic.
# Problem:
# Print numbers from 1 to 100 with these rules:
# If divisible by 3 and 5, print "FizzBuzz"
# If divisible by 3 and 7, print "FizzZap"
# If divisible by 5 only, print "Buzz"
# If divisible by 7 only, print "Zap"
# Otherwise, print the number
# Constraint:
# Use only one loop
# Do not use lists

for i in range(1, 101):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzZap")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Zap")
    else:
        print(i)