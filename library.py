books = ['science', 'math', 'social', 'computer', 'english', 'nepali']
student = []
class library():
    def __init__(self, studentName):
        self.studentName = studentName
    
    @staticmethod
    def showBooks():
        return books
    
    
    def addStudent(self):
        student.append(self.studentName)
        return student

print(f"the list of books are: {library.showBooks()}")


addstudent1 = library(studentName = input("enter the name of student: "))
print(f"students are: {addstudent1.addStudent()}")

