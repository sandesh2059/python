name = ['Jaaannne', 'Maaarrk', 'Alleeexx']
result = []

for word in name:
    unique = ''
    for ch in word:
        if ch not in unique:
            unique += ch
    result.append(unique)
print(result)
