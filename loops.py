# using break


# list = ['sandesh', 1, 2, 'chaudhary', None , 44, 'acer']

# for i in list:
#     if i != None:
#         print(i)
#         continue
#     else:
#         break


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
smallest = list[0]
for i in range(1, len(list)):
    if smallest > list[i]:
        smallest = list[i]
        print(smallest)
        continue
print(smallest)
