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