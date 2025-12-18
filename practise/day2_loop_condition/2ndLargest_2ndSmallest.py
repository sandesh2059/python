# Task 2: Second Largest & Second Smallest
# Goal: Track multiple state variables inside a loop.
# Problem:
# Given a list of integers, find the second largest and second smallest elements.
# Constraints:
# ❌ Do not sort the list
# ❌ Do not use max() or min()
# ✔ Use a single loop

number = [23, 12, 34, 65, 43, 76, 63]
if number[0] > number[1]:
    largest = number[0]
    second_largest = number[1]
    smallest = number[1]
    second_smallest = number[0]
else:
    largest = number[1]
    second_largest = [0]
    smallest = number[0]
    second_smallest = number[1]
for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print(largest)
print(smallest)
print(second_largest)
print(second_smallest)