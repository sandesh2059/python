class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = {}
    
    def addMarks(self, subject , mark):
        self.marks[subject] = mark
    
    def total_marks(self):
        return sum(self.marks.values())
    def percentage(self):
        return self.total_marks() / len(self.marks)
    def grade(self):
        perc = self.percentage()
        if perc > 80:
            return 'A+'
        elif perc > 70 and perc <=90:
            return 'A'
        elif perc > 60 and perc <=80:
            return 'B+'
        else:
            return 'Fail'
class studentManagement():
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)
    
    def displayStudent(self):
        for s in self.students:
            print(f"the name is {s.name} and the age is {s.age}, the total marks is {s.total_marks()} percentage: {s.percentage()}, grade: {s.grade()}")

sm = studentManagement()
s1 = student('sandesh', 23)
s1.addMarks('science', 55)    
s1.addMarks('math', 50)
sm.addStudent(s1)
sm.displayStudent()

    

        