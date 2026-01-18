# # # # class Book:
# # # #     def __init__(self, book_id, title, author, copies):
# # # #         self.book_id = book_id
# # # #         self.title = title
# # # #         self.author = author
# # # #         self.copies = copies

# # # #     def display(self):
# # # #         print(f"ID: {self.book_id} | {self.title} by {self.author} | Copies: {self.copies}")

# # # # class Library:
# # # #     def __init__(self):
# # # #         self.books = {}

# # # #     def add_book(self):
# # # #         book_id = input("Enter Book ID: ")
# # # #         if book_id in self.books:
# # # #             print("Book already exists!")
# # # #             return
# # # #         title = input("Enter Title: ")
# # # #         author = input("Enter Author: ")
# # # #         copies = int(input("Enter Copies: "))
# # # #         self.books[book_id] = Book(book_id, title, author, copies)
# # # #         print("Book added successfully")


# # # #     def remove_book(self):
# # # #         book_id = input("Enter Book ID to remove: ")
# # # #         if book_id in self.books:
# # # #             del self.books[book_id]
# # # #             print("Book removed")
# # # #         else:
# # # #             print("Book not found")
# # # #     def display_books(self):
# # # #         if not self.books:
# # # #             print("No books in library")
# # # #             return
# # # #         for book in self.books.values():
# # # #             book.display()
    
# # # #     def issue_book(self):
# # # #         book_id = input("Enter Book ID to issue: ")
# # # #         if book_id in self.books:
# # # #             if self.books[book_id].copies > 0:
# # # #                 self.books[book_id].copies -= 1
# # # #                 print("Book issued successfully")
# # # #             else:
# # # #                 print("No copies available")
# # # #         else:
# # # #             print("Book not found")
# # # #     def return_book(self):
# # # #         book_id = input("Enter Book ID to return: ")
# # # #         if book_id in self.books:
# # # #             self.books[book_id].copies += 1
# # # #             print("Book returned successfully")
# # # #         else:
# # # #             print("Book not found")
# # # #     def menu(self):
# # # #         while True:
# # # #             print("\n--- Library Menu ---")
# # # #             print("1. Add Book")
# # # #             print("2. Remove Book")
# # # #             print("3. Display Books")
# # # #             print("4. Issue Book")
# # # #             print("5. Return Book")
# # # #             print("6. Exit")

# # # #             choice = input("Enter choice: ")

# # # #             if choice == "1":
# # # #                 self.add_book()
# # # #             elif choice == "2":
# # # #                 self.remove_book()
# # # #             elif choice == "3":
# # # #                 self.display_books()
# # # #             elif choice == "4":
# # # #                 self.issue_book()
# # # #             elif choice == "5":
# # # #                 self.return_book()
# # # #             elif choice == "6":
# # # #                 print("Exiting Library System")
# # # #                 break
# # # #             else:
# # # #                 print("Invalid choice")


# # # # library = Library()
# # # # library.menu()


# # # class Student:
# # #     def __init__(self, sid, name, age, course):
# # #         self.sid = sid
# # #         self.name = name
# # #         self.age = age
# # #         self.course = course

# # #     def display(self):
# # #         print(f"ID: {self.sid} | Name: {self.name} | Age: {self.age} | Course: {self.course}")
# # # class StudentManagementSystem:
# # #     def __init__(self):
# # #         self.students = {}

# # #     def add_student(self):
# # #         sid = input("Enter Student ID: ")
# # #         if sid in self.students:
# # #             print("Student already exists")
# # #             return
# # #         name = input("Enter Name: ")
# # #         age = int(input("Enter Age: "))
# # #         course = input("Enter Course: ")
# # #         self.students[sid] = Student(sid, name, age, course)
# # #         print("Student added successfully")
# # #     def remove_student(self):
# # #         sid = input("Enter Student ID to remove: ")
# # #         if sid in self.students:
# # #             del self.students[sid]
# # #             print("Student removed")
# # #         else:
# # #             print("Student not found")
# # #     def update_student(self):
# # #         sid = input("Enter Student ID to update: ")
# # #         if sid not in self.students:
# # #             print("Student not found")
# # #             return
# # #         name = input("Enter new name: ")
# # #         age = int(input("Enter new age: "))
# # #         course = input("Enter new course: ")
# # #         self.students[sid].name = name
# # #         self.students[sid].age = age
# # #         self.students[sid].course = course
# # #         print("Student updated successfully")
# # #     def display_students(self):
# # #         if not self.students:
# # #             print("No student records")
# # #             return
# # #         for student in self.students.values():
# # #             student.display()
# # #     def search_student(self):
# # #         sid = input("Enter Student ID to search: ")
# # #         if sid in self.students:
# # #             self.students[sid].display()
# # #         else:
# # #             print("Student not found")
    
# # #     def menu(self):
# # #         while True:
# # #             print("\n--- Student Management Menu ---")
# # #             print("1. Add Student")
# # #             print("2. Remove Student")
# # #             print("3. Update Student")
# # #             print("4. Display Students")
# # #             print("5. Search Student")
# # #             print("6. Exit")
        
# # #             choice = input("Enter choice: ")

# # #             if choice == "1":
# # #                 self.add_student()
# # #             elif choice == "2":
# # #                 self.remove_student()
# # #             elif choice == "3":
# # #                 self.update_student()
# # #             elif choice == "4":
# # #                 self.display_students()
# # #             elif choice == "5":
# # #                 self.search_student()
# # #             elif choice == "6":
# # #                 print("Exiting Student Management System")
# # #                 break
# # #             else:
# # #                 print("Invalid choice")
# # # sms = StudentManagementSystem()
# # # sms.menu()




# # class Account:
# #     def __init__(self, acc_no, name, balance):
# #         self.acc_no = acc_no
# #         self.name = name
# #         self.balance = balance

# #     def display(self):
# #         print(f"Account No: {self.acc_no} | Name: {self.name} | Balance: Rs.{self.balance}")
# # class Bank:
# #     def __init__(self):
# #         self.accounts = {}
    
# #     def create_account(self):
# #         acc_no = input("Enter Account Number: ")
# #         if acc_no in self.accounts:
# #             print("Account already exists")
# #             return
# #         name = input("Enter Account Holder Name: ")
# #         balance = float(input("Enter Initial Balance: "))
# #         self.accounts[acc_no] = Account(acc_no, name, balance)
# #         print("Account created successfully")
    
# #     def delete_account(self):
# #         acc_no = input("Enter Account Number to delete: ")
# #         if acc_no in self.accounts:
# #             del self.accounts[acc_no]
# #             print("Account deleted")
# #         else:
# #             print("Account not found")
    
# #     def deposit(self):
# #         acc_no = input("Enter Account Number: ")
# #         if acc_no in self.accounts:
# #             amount = float(input("Enter deposit amount: "))
# #             self.accounts[acc_no].balance += amount
# #             print("Amount deposited")
# #         else:
# #             print("Account not found")
# #     def withdraw(self):
# #         acc_no = input("Enter Account Number: ")
# #         if acc_no in self.accounts:
# #             amount = float(input("Enter withdraw amount: "))
# #             if amount <= self.accounts[acc_no].balance:
# #                 self.accounts[acc_no].balance -= amount
# #                 print("Please collect cash")
# #             else:
# #                 print("Insufficient balance")
# #         else:
# #             print("Account not found")
    
# #     def display_accounts(self):
# #         if not self.accounts:
# #             print("No accounts available")
# #             return
# #         for acc in self.accounts.values():
# #             acc.display()

# #     def search_account(self):
# #         acc_no = input("Enter Account Number to search: ")
# #         if acc_no in self.accounts:
# #             self.accounts[acc_no].display()
# #         else:
# #             print("Account not found")



# class Patient:
#     def __init__(self, pid, name, age, disease):
#         self.pid = pid
#         self.name = name
#         self.age = age
#         self.disease = disease

#     def display(self):
#         print(f"ID: {self.pid} | Name: {self.name} | Age: {self.age} | Disease: {self.disease}")

# class Hospital:
#     def __init__(self):
#         self.patients = {}
#     def add_patient(self):
#         pid = input("Enter Patient ID: ")
#         if pid in self.patients:
#             print("Patient already exists")
#             return
#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         disease = input("Enter Disease: ")
#         self.patients[pid] = Patient(pid, name, age, disease)
#         print("Patient added successfully")
#     def remove_patient(self):
#         pid = input("Enter Patient ID to remove: ")
#         if pid in self.patients:
#             del self.patients[pid]
#             print("Patient removed")
#         else:
#             print("Patient not found")
#     def update_patient(self):
#         pid = input("Enter Patient ID to update: ")
#         if pid not in self.patients:
#             print("Patient not found")
#             return
#         name = input("Enter new Name: ")
#         age = int(input("Enter new Age: "))
#         disease = input("Enter new Disease: ")
#         self.patients[pid].name = name
#         self.patients[pid].age = age
#         self.patients[pid].disease = disease
#         print("Patient updated successfully")
#     def display_patients(self):
#         if not self.patients:
#             print("No patient records")
#             return
#         for patient in self.patients.values():
#             patient.display()

#     def search_patient(self):
#         pid = input("Enter Patient ID to search: ")
#         if pid in self.patients:
#             self.patients[pid].display()
#         else:
#             print("Patient not found")
#     def menu(self):
#         while True:
#             print("\n--- Hospital Management Menu ---")
#             print("1. Add Patient")
#             print("2. Remove Patient")
#             print("3. Update Patient")
#             print("4. Display Patients")
#             print("5. Search Patient")
#             print("6. Exit")
#             choice = input("Enter choice: ")

#             if choice == "1":
#                 self.add_patient()
#             elif choice == "2":
#                 self.remove_patient()
#             elif choice == "3":
#                 self.update_patient()
#             elif choice == "4":
#                 self.display_patients()
#             elif choice == "5":
#                 self.search_patient()
#             elif choice == "6":
#                 print("Exiting Hospital Management System")
#                 break
#             else:
#                 print("Invalid choice")

# hospital = Hospital()
# hospital.menu()




class Bus:
    def __init__(self, bus_no, route, seats):
        self.bus_no = bus_no
        self.route = route
        self.seats = seats

    def display(self):
        print(f"Bus No: {self.bus_no} | Route: {self.route} | Available Seats: {self.seats}")    

class BusReservationSystem:
    def __init__(self):
        self.buses = {}
    def add_bus(self):
        bus_no = input("Enter Bus Number: ")
        if bus_no in self.buses:
            print("Bus already exists")
            return
        route = input("Enter Route: ")
        seats = int(input("Enter Total Seats: "))
        self.buses[bus_no] = Bus(bus_no, route, seats)
        print("Bus added successfully")
    def remove_bus(self):
        bus_no = input("Enter Bus Number to remove: ")
        if bus_no in self.buses:
            del self.buses[bus_no]
            print("Bus removed")
        else:
            print("Bus not found")
    def display_buses(self):
        if not self.buses:
            print("No buses available")
            return
        for bus in self.buses.values():
            bus.display()
    def book_ticket(self):
        bus_no = input("Enter Bus Number: ")
        if bus_no in self.buses:
            if self.buses[bus_no].seats > 0:
                self.buses[bus_no].seats -= 1
                print("Ticket booked successfully")
            else:
                print("No seats available")
        else:
            print("Bus not found")
    def cancel_ticket(self):
        bus_no = input("Enter Bus Number: ")
        if bus_no in self.buses:
            self.buses[bus_no].seats += 1
            print("Ticket cancelled successfully")
        else:
            print("Bus not found")