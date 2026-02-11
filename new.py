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
