# # is prime?

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(num=int(input("enter a number: "))))

#if even square that number and put it in list


# def list_comprehension(list):
    
    
#     square = [n*n for n in a if n % 2 == 0]
#     return square
# a = [1, 2, 3, 4, 5, 6]
# print(list_comprehension(a))


# num = [1, 2, 3, 4, 5]
# new_num = [n+10 for n in num ]
# print(new_num)


# def reverse_string(word):
#     rev = ''
#     for i in word:
#         rev = i + rev
#     return rev
# print(reverse_string(word = 'sandesh'))


def is_prime_list(numbers):
    primes = []
    for num in numbers:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
        
listing = []
n = int(input("how many elements do you need in a list: "))
for i in range(n):
    number = int(input(f"enter a number {i+1}: "))
    listing.append(number)

print(is_prime_list(listing))
            