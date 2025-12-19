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

def menu():
    while True:
        print("\n------ NUMBER ANALYZER MENU ------")
        print("1. Analyze a number")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter a number to analyze: "))
            print("Reversed number: ", reverse(num))
            palindrome(num)
            print("Total digits: ", total_digits(num))
            print("Sum of digits: ", total_sum(num))

        elif choice == '2':
            print("EXITING")
            break

        else:
            print("Invalid choice, try again.")

menu()