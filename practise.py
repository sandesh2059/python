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