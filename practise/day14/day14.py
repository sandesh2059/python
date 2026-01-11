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
    
    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return

        print("\nBook ID | Name | Author | Status")
        print("--------------------------------")
        for book_id, details in self.books.items():
            status = "Available" if details["available"] else "Issued"
            print(f"{book_id} | {details['name']} | {details['author']} | {status}")