# marks = [23, 45, 12, 56, 89, 3, 44]

# smallest = float('inf')
# largest = float('-inf')

# for i in range(1, len(marks)):
#     if marks[i] > largest:
#         largest = marks[i]
    
#     elif marks[i] < smallest:
#         smallest = marks[i]
# print(smallest)
# print(largest)




name = ['ram', 'shyam', 'hari', 'sandesh', 'chaudhary']
for i in range(len(name)):
    
    name[i] = name[i][::-1]

print(name)



listing = ['ssshyyyuuuuhh','yyyjjkkkeee','ooiieee']
result = []

for word in listing:
    unique = ''
    for ch in word:
        if ch not in unique:
            unique += ch
    result.append(unique)
print(result)



