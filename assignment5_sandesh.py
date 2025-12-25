def recursive_palindrome(word):
    if len(word) <= 1:
        return True
    
    if word[0] != word[-1]:
        return False
    
    return recursive_palindrome(word[1:-1])


def sum_of_digits(n):
    total = 0
    for i in range(n):
        total += n % 10
        n //= 10
    return total

def menu():
    while True:
        print("1. recursive palindorme")
        print("2. sum of digits of a number")
        print("3. exit")

        choice = int(input("enter your choice: "))  

        if choice == 1:
            words = input("enter a word: ")
            if recursive_palindrome(words):
                print(f"{words} is palindorm")
            else:
                print(f"{words} is not palindrome")
            
    
        elif choice == 2:
            num = int(input("enter a number: "))
            if num < 10:
                print(f"the sum is {num} ")
            else:
                print(f"the sum of digits is: {sum_of_digits(num)}")
    
        elif choice == 3:
            print("Exiting")
            break

        else:
            print("invalid choice")

menu()
