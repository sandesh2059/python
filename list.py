# # to create a list called colors
# colors = ["red", "green", "blue"]
# print(colors[1])

# # to change the first element of the list to "yellow"
# colors[0] = "yellow"

# # to print the last two elements of the list
# print(colors[2:3])

# # to print the lenght of the list
# print(len(colors))




#to create a list of random numbers
list = [3,1,4,6,8,2,5,7]
print(list)

# to sort the list
list.sort()
print(list)

# to find the maxiumu value in a list

print(max(list))

# to find the minimum value in the list

print(min(list))

#to find the sum of all elements of the list

print(sum(list))



# to find all the even numbers and odd numbers in a list
for i in list:
    if i % 2 == 0:
        print("even number", i)

    else:
        print("odd number", i)


# to reverse the list

list.reverse()
print(list)


#to sort the list in ascending and descending order

list.sort()
print(list)

list.sort(reverse=True)
print(list)








