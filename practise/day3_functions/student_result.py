# You are building a system that:

# Stores multiple students

# Each student has:

# Name

# Marks in 3 subjects

# System should:

# Add student

# Calculate total marks

# Calculate percentage

# Determine grade

# Display all students


def get_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(1):
        python = int(input(f"enter marks in python: "))
        django = int(input(f"enter marks in django: "))
        intern = int(input(f"enter marks in intern: "))

        marks.append(python)
        marks.append(django)
        marks.append(intern)

    return {
        'name': name,
        'marks': marks
        }
    
def calculate_total(marks):
    total = sum(marks)
    return total

def calculate_percent(total):
    return total / 3
    
def grade(percent):
    if percent > 90:
        print('good')

def display_student(students):
    for s in students:
        total = calculate_total(s["marks"])
        percent = calculate_percent(total)
        grade =  grade(percent)

        print("\nname: ", s['name'])
        print("total = ", total)
        print("percentage = ", round(percent, 2))
        print("grade = ", grade)

def menu():

    students = []

    while True:
        print("1. add student")
        print("2. view student")
        print("3. exit")

        choice = input("enter your choice: ")
        if choice == '1':
            student1 = get_student()
            students.append(student1)
            print("student added successfully")

        if choice == '2':
            if not students:
                print("no students available")
            else:
                display_student(students)

        if choice == '3':
            print("Exiting")
            break

        else:
            print("invalid choice")

menu()



    
        



