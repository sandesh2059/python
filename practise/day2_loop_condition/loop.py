# #                           printing numbers from 1 to 10 using for loop
# for i in range(10):
#     print(i+1)



# #               print all even numbers from 1 to 20

# for i in range(2, 21, 2):
#     print(i)


# #                   Print each character of the string "Python" on a new line.

# string = 'python'
# for i in range(0, len(string)):
#     print(string[i])



# #                       Find the sum of numbers from 1 to 50.
# c = 0
# for i in range(1,51):
#     c += i
    
# print(c)


# #                       Print the multiplication table of 5.

# a = 5
# for i in range(1,11):
#     print(i * a)


# #                       Count how many vowels are there in a string entered by the user.

# word = input("Enter a random word: ")
# count = 0
# for i in range(1, len(word)):
#     if word[i] in "aeiou":
#         count += 1
# print(f"the total number of vowels are {count}")




# #                   Print all numbers between 1 and 100 that are divisible by 7.

# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i)




# #                       Find the factorial of a number using a for loop.

# a = int(input("Enter a number: "))
# c = 1
# for i in range(1, a+1):
#     c = c * i
# print(c)




# #                       Given a list [2, 4, 6, 8, 10], calculate the sum of elements.

# a = 0
# list = [2, 4, 6, 8, 10]
# for i in range(len(list)):
#     a = a + list[i]
# print(a)



# #                           Print the reverse of a string using a for loop.

# string = input("Enter a word: ")
# reverse = ""
# for i in range(len(string)-1, -1, -1):
#     reverse += string[i]
# print(reverse)
    



# #                           Find the largest number in a list using a for loop.

# list = [23, 534, 532, 234, 65, 423, 432, 144]
# largest = list[0]
# for i in range(1, len(list)):
#     if list[i] > largest:
#         largest = list[i]
# print(largest)



# #                           Calculate the average marks of 5 subjects stored in a list.

# marks = 0
# marks_list = [28, 34, 33, 34, 31,]
# for i in marks_list:
#     marks += i
#     print("marks: ", marks)
# average = marks / len(marks_list)

# print(average)





# #                       Print all prime numbers between 1 and 50.

# for num in range(2, 51):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num , end = " ")
    





# #                       Given prices [500, 680, 1200, 999], apply 10% discount to each and print the final prices.

# price = [500, 680, 1200, 999]
# for i in price:
#     discount = (10 / 100) * i
#     discounted_price = i - discount
#     print(discounted_price, end = " ")






# #                       Count how many even and odd numbers are in a list.


# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# count_even = 0
# count_odd = 0

# for i in number:
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print("even : ", count_even)
# print("odd : ", count_odd)






# #                           Check whether a string is a palindrome using a for loop.

# word = input(" Enter a word: ")
# reverse = ""
# for i in range(len(word)-1, -1, -1):
#     reverse += word[i]
# print(f"real word is {word} and reversed word is {reverse}")

# if word == reverse:
#     print("palindorme word")
# else:
#     print("not a palindrome")




