# class Library:

#     def __init__(self):
#         # Dictionary to store books
#         self.books = {}
    
#     def add_book(self):
#         book_id = input("Enter Book ID: ")
#         name = input("Enter Book Name: ")
#         author = input("Enter Author Name: ")

#         self.books[book_id] = {
#             "name": name,
#             "author": author,
#             "available": True
#         }

#         print("Book added successfully!")
    
#     def display_books(self):
#         if not self.books:
#             print("Library is empty.")
#             return

#         print("\nBook ID | Name | Author | Status")
#         print("--------------------------------")
#         for book_id, details in self.books.items():
#             status = "Available" if details["available"] else "Issued"
#             print(f"{book_id} | {details['name']} | {details['author']} | {status}")
    
#     def search_book(self):
#         book_id = input("Enter Book ID to search: ")

#         if book_id in self.books:
#             book = self.books[book_id]
#             status = "Available" if book["available"] else "Issued"
#             print("\nBook Found")
#             print("Name:", book["name"])
#             print("Author:", book["author"])
#             print("Status:", status)
#         else:
#             print("Book not found.")




class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"