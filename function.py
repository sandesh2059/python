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


# def greet_student(name):
#     print(f"welcome to the python class {name}")
#     return f"good day {name}"

# name = input('enter name: ')
# greet = greet_student(name)
# print(greet)




# def iterate_list(name: list) -> list:



# def volume_cuboid(length, breadth, height):
#     return length * breadth * height



# length = int(input("enter length: "))
# breadth = int(input("enter breadth: "))
# height = int(input("enter height: "))
# print(volume_cuboid(length, breadth, height))





# def reverse(marks):
#     for i in range(len(marks)):
#         marks[i] = marks[i][::-1]
#         return marks

# marks = ['123', '3423', '413', '1454']

# print(reverse(marks))



def message(num):
    for i in range(num):
        print("hello my name is sandesh ")
    return ''
n = int(input("enter how many times do you want to print the message: "))
print(message(n))


















