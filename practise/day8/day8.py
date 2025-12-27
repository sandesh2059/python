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