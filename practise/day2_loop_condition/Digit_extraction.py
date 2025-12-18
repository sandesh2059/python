# Task 4: Count Digits & Special Properties
# Goal: Deepen understanding of digit extraction.
# Problem:
# Given a number, find:
# Total number of digits
# Sum of digits
# Count of even digits
# Count of odd digits

num = int(input("Enter a number: "))
count = 0
count_even = 0
count_odd = 0
sum_num = 0

while num != 0:
    last_digit = num % 10
    count += 1
    sum_num += last_digit
    num //= 10
    if last_digit % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("the sum of digits is: ", sum_num)
print("the number of digit is: ", count)
print("the number of even digit is: ", count_even)
print("the number of odd digit is: ", count_odd)