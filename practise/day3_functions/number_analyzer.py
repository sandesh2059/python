def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return rev


def palindrome(n):
    if n == reverse(n):
        print("Palindrome: YES")
    else:
        print("Palindrome: NO")




def total_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count



def total_sum(n):
    add = 0
    while n > 0:
        add += n % 10
        n //= 10
    return add