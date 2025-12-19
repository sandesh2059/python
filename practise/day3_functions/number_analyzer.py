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