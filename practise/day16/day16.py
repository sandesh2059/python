class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        print(f"ID: {self.book_id} | {self.title} by {self.author} | Copies: {self.copies}")

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        if book_id in self.books:
            print("Book already exists!")
            return
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        copies = int(input("Enter Copies: "))
        self.books[book_id] = Book(book_id, title, author, copies)
        print("Book added successfully")