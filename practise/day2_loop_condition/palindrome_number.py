# Task 3: Palindrome Number Checker (Math Only)
# Goal: Combine loops, math, and condition checking.
# Problem:
# Ask the user for a number and check whether it is a palindrome.
# Example:
# Input: 1221
# Output: Palindrome
# Constraints:
# ❌ Do not convert the number to a string
# ✔ Use while, %, and //
# ✔ Compare original and reversed numbers

num = int(input("Enter a number: "))
original_num = num
reverse = 0

while num != 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num //= 10
if reverse == original_num:
    print(f"{original_num} is a palindrome number")
    print(f"input {original_num} = reversed {reverse}")
else:
    print(f"{original_num} is not a palindrome number")