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