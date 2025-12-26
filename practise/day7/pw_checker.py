def check_strength(password):
    has_digit = False
    has_upper = False

    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long"

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True

    if has_digit and has_upper:
        return "Strong Password"
    else:
        return "Weak: Must contain at least one digit and one uppercase letter"

def menu():
    while True:
        print("\n--- Password Strength Checker ---")
        print("1. Check Password")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            password = input("Enter password: ")
            result = check_strength(password)
            print(result)

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice")


menu()
