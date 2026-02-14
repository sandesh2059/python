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

def remove_duplicates(lst):
    result = []
    
    for item in lst:
        if item not in result:
            result.append(item)
    
    return result

print(remove_duplicates([1,2,2,3,4,4,5]))


def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i

print(two_sum([2,7,11,15], 9))


def find_missing(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum

print(find_missing([1,2,3,5,6]))

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for char in s1:
        count[char] = count.get(char, 0) + 1
    
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True

print(is_anagram("listen", "silent"))


def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("Sandesh"))


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("python")) # False


def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([10, 20, 4, 45, 99, 99]))


def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_frequency("banana"))

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(20)

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

print(find_duplicates([1,2,3,4,2,5,1,6]))
