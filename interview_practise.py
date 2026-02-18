# # is prime?

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(num=int(input("enter a number: "))))

#if even square that number and put it in list


# def list_comprehension(list):
    
    
#     square = [n*n for n in a if n % 2 == 0]
#     return square
# a = [1, 2, 3, 4, 5, 6]
# print(list_comprehension(a))


# num = [1, 2, 3, 4, 5]
# new_num = [n+10 for n in num ]
# print(new_num)


# def reverse_string(word):
#     rev = ''
#     for i in word:
#         rev = i + rev
#     return rev
# print(reverse_string(word = 'sandesh'))


# def is_prime_list(numbers):
#     primes = []
#     for num in numbers:
#         if num <= 1:
#             continue
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes
        
# listing = []
# n = int(input("how many elements do you need in a list: "))
# for i in range(n):
#     number = int(input(f"enter a number {i+1}: "))
#     listing.append(number)

# print(is_prime_list(listing))
            

# def is_palindrome_list(words):
#     palindrome = []
#     for word in words:
#         if word == word[::-1]:
#             palindrome.append(word)
#     return palindrome
        

# w = int(input("how many words do you want in your list: "))
# words = []
# for i in range(w):
#     string = input(f"enter the number {i+1} word: ")
#     words.append(string)

# print(is_palindrome_list(words))




# def is_palindrome(word):
#     rev = ''
#     for i in word:
#         rev = i + rev
#     return rev

# print(is_palindrome('sandesh'))

# OR

# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False

# print(is_palindrome('sandesh'))



# def count_frequency(text):
#     freq = {}
#     for char in text:
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     return freq

# print(count_frequency('sandesh'))







# # Task 1: List Filtering & Transformation
# # Given a list of integers: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Write a List Comprehension that creates a new list containing the squares of only the even numbers.


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = [n * n for n in numbers if n % 2 == 0]
# print(square)







# Task 2: Character Frequency & Logic
# The Goal: Given a string, create a dictionary of character counts.
# The Twist: Exclude spaces and hyphens.

# Python
# sentence = "django is a high-level python web framework"
# Write the code to generate that dictionary. How will you handle the exclusion of those specific characters?
# def frequency(sentence):

#     freq = {}
#     for char in sentence:
#         if char == ' ' or char == '-':
#             continue
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     return freq
# sentence = "django is a high-level python web framework"
# print(frequency(sentence))






# Task 3: Finding Duplicates
# Let's move to a common list challenge.

# The Goal: Given a list, find which items appear more than once.

# Python
# items = ["apple", "banana", "cherry", "apple", "orange", "cherry", "cherry"]
# Constraint: Your function should return a list of the duplicates: ["apple", "cherry"].


# items = ["apple", "banana", "cherry", "apple", "orange", "cherry", "cherry"]

# def dup_list(items):
#     items1 = {}
#     items2 = []
#     for item in items:
#         if item in items1:
#             items1[item] +=1
#         else:
#             items1[item] = 1
#     for item in items1:
#         if items1[item] > 1:
#             items2.append(item)
#     return items2

# print(dup_list(items))












# Task 4: The "API Result" Re-map
# This is a very common task in Django when you've fetched a list of objects (like from a database or a JSON API) and need to transform them for quick lookup.

# The Scenario:

# Python
# api_data = [
#     {"id": 101, "name": "Laptop", "price": 1200},
#     {"id": 102, "name": "Mouse", "price": 25},
#     {"id": 103, "name": "Monitor", "price": 300},
# ]
# The Goal: Create a new dictionary where the id is the key and the price is the value.
# Target Output: {101: 1200, 102: 25, 103: 300}



# api_data = [
#     {"id": 101, "name": "Laptop", "price": 1200},
#     {"id": 102, "name": "Mouse", "price": 25},
#     {"id": 103, "name": "Monitor", "price": 300},
# ]

# price_map = {item['id']: item['price'] for item in api_data}

# print(price_map)






# Task 5: Grouping Data

# The Goal: Given a list of names, group them by their first letter.

# Python
# names = ["Alice", "Bob", "Charlie", "Alex", "Ben"]
# Target Output:
# {'A': ['Alice', 'Alex'], 'B': ['Bob', 'Ben'], 'C': ['Charlie']}

names = ["Alice", "Bob", "Charlie", "Alex", "Ben"]

new = {}
for name in names:
    letter = name[0]
    
    if letter not in new:
        new[letter] = []
    new[letter].append(name)


print(new)



