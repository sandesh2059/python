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
