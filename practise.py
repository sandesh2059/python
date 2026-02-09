integer_num = 10
float_num = 10.5
string_text = "Python"
boolean_val = True

numbers_list = [1, 2, 3, 4, 5]
unique_numbers = {1, 2, 3, 3, 4}
student_info = {
    "name": "Sandesh",
    "age": 22,
    "course": "CS"
}
def separate_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def reverse_string(text):
    return text[::-1]

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

even_nums, odd_nums = separate_even_odd(numbers_list)
char_result = count_characters("interview")
reversed_word = reverse_string("Python")
max_value = find_max(numbers_list)

print("Even:", even_nums)
print("Odd:", odd_nums)
print("Char Count:", char_result)
print("Reversed:", reversed_word)
print("Max Value:", max_value)

class Person:
    def __init__(self, name, age):
        self.name = name        # public attribute
        self._age = age         # protected attribute

    def display_info(self):
        return f"Name: {self.name}, Age: {self._age}"
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        return f"Student {self.name}, ID: {self.student_id}, Age: {self._age}"

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return "Deposit successful"
        return "Invalid amount"
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return "Withdrawal successful"
        return "Insufficient balance"

    def get_balance(self):
        return self.__balance
    
person1 = Person("Ram", 30)
student1 = Student("Shyam", 21, "STU101")
account1 = BankAccount("Sandesh", 5000)

print(person1.display_info())
print(student1.display_info())

print(account1.deposit(2000))
print(account1.withdraw(1000))
print("Balance:", account1.get_balance())

for i in range(1, 11):
    if i % 3 == 0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is not divisible by 3")

# ---------- LIST COMPREHENSION ----------
squared_numbers = [n ** 2 for n in numbers_list]
even_only = [n for n in numbers_list if n % 2 == 0]

print("Squared:", squared_numbers)
print("Even Only:", even_only)

try:
    value = int("abc")
except ValueError:
    print("Conversion failed!")
finally:
    print("Execution completed")


INT_VAL = 100
FLOAT_VAL = 25.75
STR_VAL = "Python Interview"
BOOL_VAL = True

LIST_VAL = [5, 10, 15, 20, 25]
TUPLE_VAL = (1, 2, 3)
SET_VAL = {1, 2, 3, 4}
DICT_VAL = {"lang": "Python", "level": "Intermediate"}

def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def average_list(numbers):
    if not numbers:
        return 0
    return sum_list(numbers) / len(numbers)

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def fibonacci(limit):
    series = []
    a, b = 0, 1
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    return series




def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string("interview"))
