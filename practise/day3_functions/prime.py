def isPrime(n):
    if n <= 1:
        return False
    for i in range(1, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True
print(isPrime(7))
