# s = 'hello'
# rev = ''

# for ch in s:
#     rev = ch + rev
# print(rev)





def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("sandesh"))

def second_largest(nums):
    first = second = float('-inf')
    
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second

print(second_largest([10, 20, 4, 45, 99]))

def char_frequency(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    return freq

print(char_frequency("programming"))



def is_palindrome(num):
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return original == reversed_num

print(is_palindrome(121))
