# library management system

library = []


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    library.append({
        "title": title,
        "author": author,
        "issued": False
    })

    print("Book added successfully")
def issue_book():
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']}")

    choice = int(input("Select book number: "))
    library[choice - 1]["issued"] = True
    print("Book issued")

def return_book():
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']}")

    choice = int(input("Select book number: "))
    library[choice - 1]["issued"] = False
    print("Book returned")

def view_books():
    print("\n--- Library Books ---")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f"{book['title']} ({book['author']}) - {status}")

def menu():
    while True:
        print("\n--- Library System ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            issue_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            view_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice")


menu()