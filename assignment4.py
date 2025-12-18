show_menu = True
while show_menu:

    print("MENU")
    print("1. (TASK 1:Task 1: The FizzBuzz Classic (Pattern Logic) )")
    print("2. (TASK 2: Find the Maximum and Minimum (Array Traversal) )")
    print("3. (TASK 3: Reverse a Number (Mathematical Loop) )")
    print("4. (TASK 4: Prime Number Checker (Efficiency Logic) )")
    print("5. (TASK 5: The Fibonacci Sequence (Algorithmic Thinking)) ")

    choice = int(input("Choose a Task by entering a corresponding number: "))

    # for task 1
    if choice == 1:
        for i in range(1, 51):
            if i % 5 == 0 and i % 3 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")        
            else:
                print(i)
    

    # for task 2
    elif choice == 2:
        marks = [23, 45, 12, 56, 89, 3, 44]
        if marks[0] > marks[1]:
        
            smallest = marks[1]
            largest = marks[0]

        else:

            smallest = marks[0]
            largest = marks[1]

        for i in range(2, len(marks)):
            if marks[i] < smallest:
                smallest = marks[i]
            elif marks[i] > largest:
                largest = marks[i]
   
        print("the smallest number is: ", smallest)
        print("the largest number is : ", largest)
    

    # for task 3
    elif choice == 3:
        num = int(input("Enter a number: "))
        reverse = 0
        while num != 0:
            last_digit = num % 10
            reverse = reverse * 10 + last_digit
            num //= 10
        print("the reversed number is: ", reverse)

    
    # for task 4
    elif choice == 4:
        a = int(input("Enter a number: "))
        if a <= 1:
            print(f"{a} is not a prime")
        else:
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    print(f"{a} is not a prime number")
                    break
            else:  
                print(f"{a} is a prime")

    # for task 5
    elif choice == 5:
        a = 0
        b = 1
        c = a + b
        N = int(input("Enter a Nth term of fibinacci series: "))

        if N <= 1:
            print("Please choose a number higher than 1")
        else:
            print(a, end=" ")
            print(b, end=" ")

        for i in range(2, N):
            c = a + b
            a = b 
            b = c
            print(c, end =" ")

    else:
        print("Please enter valid number")

    again = input("\nDo you want to see the menu again? enter y for yes, n for no: ").lower()
    if again != "y":
        show_menu = False
        print("SEE YA")




    



 