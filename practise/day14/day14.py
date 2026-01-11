class Library:

    def __init__(self):
        # Dictionary to store books
        self.books = {}
    
    def add_book(self):
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        self.books[book_id] = {
            "name": name,
            "author": author,
            "available": True
        }

        print("Book added successfully!")