books = ['science', 'math', 'social', 'computer', 'english', 'nepali']
student = []
class library():
    def __init__(self):
        self.studentName = 'sandesh'
    
    @staticmethod
    def showBooks():
        return books
    
    @staticmethod
    def number_of_books():
        return len(books)
    
    @staticmethod
    def add_book(bookname):
        books.append(bookname)
        return bookname
    
    
    def addStudent(self):
        student.append(self.studentName)
        return student

print(f"the list of books are: {library.showBooks()}\nthe number of books in library is: {library.number_of_books()}")


b1 = library()
b1.add_book('lotm')
print(f"the updated list of book is: {books}")

print(f"the new number of books is: {library.number_of_books()}")


addstudent1 = library()
addstudent1.addStudent()
print("students: ", student)



