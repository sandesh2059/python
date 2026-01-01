# high order functions = lambda, map, filer, reduce

def cube(a):
    return a * a * a
print(cube(5))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_l = list(map(cube, l))
print(new_l)

def greater(a):
    return a > 2

ll = list(filter(greater, l))
print(ll)

from functools import reduce

def sum(x , y):
    return x + y

sum_of_digits = reduce(sum, l)
print(sum_of_digits)