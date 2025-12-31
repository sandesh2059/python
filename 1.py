class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def total_marks(self):
        return sum(self.marks)
    def percentage(self):
        return self.total_marks() / len(self.marks)
    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return "A"
        elif percent >= 75:
            return "B"
        elif percent >= 60:
            return "C"
        else:
            return "Fail"
class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        name = input("Enter student name: ")
        marks = []
        for i in range(3):
            m = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)

        student = Student(name, marks)
        self.students.append(student)
        print("Student added successfully ✅")
