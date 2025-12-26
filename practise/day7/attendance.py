students = []


def add_student(students):
    name = input("Enter student name: ")
    students.append({
        "name": name,
        "present": False
    })
    print("Student added successfully")
def mark_attendance(students):
    if not students:
        print("No students available")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']}")

    choice = int(input("Select student number: "))
    status = input("Mark Present (P) or Absent (A): ").upper()

    if status == 'P':
        students[choice - 1]["present"] = True
    else:
        students[choice - 1]["present"] = False

    print("Attendance updated")