def showmenu():
    print("\nMENU")
    print("1. FIND MAX AND MIN FROM THE LIST")
    print("2. TO REVERSE A NUMBER MATHEMATICALLY")
    print("3. TO GENERATE FIBONACCI UPTO nth TERMS")
    print("4. TO CHECK IF A NUMBER IS PALINDROME")
showmenu()
while True:
    choice = input("Enter a number for the Task that you want to perform: ")
    
    # minmax finding from the list
    if choice == '1':
        def minmax():
            print("Finding maximum and minimum from the list")
            largest = float('-inf')
            smallest = float('inf')
            n = int(input("how many elements do you want to put in list: "))
            elements = []
            for i in range(0, n):
                x = int(input("Enter your element: "))
                elements.append(x)
                if elements[i] > largest:
                    largest = elements[i]
                if elements[i] < smallest:
                    smallest = elements[i]
            print(elements)
            print(f"In this list, the maximum number is {largest}")
            print(f"In this list, the smallest number is {smallest}")
        minmax()
        break


    # reverse number 
    if choice == '2':
        print("reversing a number")
        def reverse(n):
            n = int(input("Enter a number: "))
            reversed_n = 0
            for i in range(len(n)):
                last_digit = n % 10
                reversed_n = reversed_n * 10 + last_digit
                n //= 10
            print("The reversed number is: ", reversed_n)
        print(reverse(1312))
        break
                


        