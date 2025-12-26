students = []


def add_student(students):
    name = input("Enter student name: ")
    students.append({
        "name": name,
        "present": False
    })
    print("Student added successfully")
