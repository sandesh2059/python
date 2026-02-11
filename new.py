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
