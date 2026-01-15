# class Book:
#     def __init__(self, book_id, title, author, copies):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.copies = copies

#     def display(self):
#         print(f"ID: {self.book_id} | {self.title} by {self.author} | Copies: {self.copies}")

# class Library:
#     def __init__(self):
#         self.books = {}

#     def add_book(self):
#         book_id = input("Enter Book ID: ")
#         if book_id in self.books:
#             print("Book already exists!")
#             return
#         title = input("Enter Title: ")
#         author = input("Enter Author: ")
#         copies = int(input("Enter Copies: "))
#         self.books[book_id] = Book(book_id, title, author, copies)
#         print("Book added successfully")


#     def remove_book(self):
#         book_id = input("Enter Book ID to remove: ")
#         if book_id in self.books:
#             del self.books[book_id]
#             print("Book removed")
#         else:
#             print("Book not found")
#     def display_books(self):
#         if not self.books:
#             print("No books in library")
#             return
#         for book in self.books.values():
#             book.display()
    
#     def issue_book(self):
#         book_id = input("Enter Book ID to issue: ")
#         if book_id in self.books:
#             if self.books[book_id].copies > 0:
#                 self.books[book_id].copies -= 1
#                 print("Book issued successfully")
#             else:
#                 print("No copies available")
#         else:
#             print("Book not found")
#     def return_book(self):
#         book_id = input("Enter Book ID to return: ")
#         if book_id in self.books:
#             self.books[book_id].copies += 1
#             print("Book returned successfully")
#         else:
#             print("Book not found")
#     def menu(self):
#         while True:
#             print("\n--- Library Menu ---")
#             print("1. Add Book")
#             print("2. Remove Book")
#             print("3. Display Books")
#             print("4. Issue Book")
#             print("5. Return Book")
#             print("6. Exit")

#             choice = input("Enter choice: ")

#             if choice == "1":
#                 self.add_book()
#             elif choice == "2":
#                 self.remove_book()
#             elif choice == "3":
#                 self.display_books()
#             elif choice == "4":
#                 self.issue_book()
#             elif choice == "5":
#                 self.return_book()
#             elif choice == "6":
#                 print("Exiting Library System")
#                 break
#             else:
#                 print("Invalid choice")


# library = Library()
# library.menu()


class Student:
    def __init__(self, sid, name, age, course):
        self.sid = sid
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"ID: {self.sid} | Name: {self.name} | Age: {self.age} | Course: {self.course}")
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        sid = input("Enter Student ID: ")
        if sid in self.students:
            print("Student already exists")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        self.students[sid] = Student(sid, name, age, course)
        print("Student added successfully")
    def remove_student(self):
        sid = input("Enter Student ID to remove: ")
        if sid in self.students:
            del self.students[sid]
            print("Student removed")
        else:
            print("Student not found")
    def update_student(self):
        sid = input("Enter Student ID to update: ")
        if sid not in self.students:
            print("Student not found")
            return
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
        self.students[sid].name = name
        self.students[sid].age = age
        self.students[sid].course = course
        print("Student updated successfully")
    def display_students(self):
        if not self.students:
            print("No student records")
            return
        for student in self.students.values():
            student.display()
    def search_student(self):
        sid = input("Enter Student ID to search: ")
        if sid in self.students:
            self.students[sid].display()
        else:
            print("Student not found")
    
    def menu(self):
        while True:
            print("\n--- Student Management Menu ---")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Update Student")
            print("4. Display Students")
            print("5. Search Student")
            print("6. Exit")
        
            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.display_students()
            elif choice == "5":
                self.search_student()
            elif choice == "6":
                print("Exiting Student Management System")
                break
            else:
                print("Invalid choice")