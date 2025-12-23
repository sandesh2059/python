# #  to find min max using function


# def minmax():
#     listing = []

#     largest = float('-inf')
#     smallest = float('inf')

#     n = int(input("Enter how many elements in a list do you want: "))

#     for i in range(0, n):
#         element = int(input("enter the elements: "))
#         listing.append(element)

#         if listing[i] > largest:
#             largest = listing[i]
#         if listing[i] < smallest:
#             smallest = listing[i]
        
#     print("the smallest number in the list is: ", smallest)
#     print("the largest number in the list is: ", largest)

# minmax()




# to reverse a number

# def reverse(n):
#     rev = 0
#     while n > 0:

#         rev = rev * 10 + (n % 10)
#         n //= 10
    
#     return rev
# num = int(input("enter a number: "))
# reverse(num)
# print("the reversed number is: ", reverse(num))

















# marks = [12, 33, 12, 44, 11]

# total = sum(marks)

# new_marks = int(input("enter a new marks: "))

# marks.append(new_marks)

# for i in range(len(marks)):


def greet_student(name):
    print(f"welcome to the python class {name}")

name = input('enter name: ')
greet_student(name)





