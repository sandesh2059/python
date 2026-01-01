# high order functions = lambda, map, filer, reduce

def cube(a):
    return a * a * a
print(cube(5))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_l = list(map(cube, l))
print(new_l)