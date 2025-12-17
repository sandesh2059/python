dict_1 = {'name':'sandesh', 'age':23}
dict_2 = {'age':23, 'name':'chaudhary'}

# print(dict_1 == dict_2)

print(id(dict_1))
# print(id(dict_2))
# print(dict_1 is dict_2)


# merging the dictionaries
# 1. using union

# merged_dict = dict_1 | dict_2
# print(merged_dict)
# print(id(merged_dict))

# 2. using update merge

# dict_1.update(dict_2)
# print(dict_1)
# print(id(dict_1))

# 3. keyword argument merge

# result_dict = {**dict_2,**dict_1}
# print(result_dict)

# result_dict = {**dict_1,**dict_2}
# print(result_dict)


# removing key value pair
dict_3 = {'name':"Sandesh", 'age':23, }
# value = dict_3.pop('name')
# print(dict_3)

value = dict_3.popitem()
print(value)
print(dict_3)