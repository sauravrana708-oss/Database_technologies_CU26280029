# Program 7: Menu-driven CRUD on a list of books
# Example I/O:
#   Menu: 1.Add 2.View 3.Update 4.Delete 5.Exit

books = [{"title": "Python Basics", "author": "A. Kumar"}]

while True:
    print("\n1. Add  2. View  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        books.append({"title": input("Title: "), "author": input("Author: ")})
        print("Book added.")
    elif choice == "2":
        if not books:
            print("No books.")
        for i, b in enumerate(books, 1):
            print(i, b["title"], "-", b["author"])
    elif choice == "3":
        try:
            i = int(input("Book number to update: ")) - 1
            books[i]["title"] = input("New title: ")
            books[i]["author"] = input("New author: ")
            print("Book updated.")
        except (ValueError, IndexError):
            print("Invalid book number.")
    elif choice == "4":
        try:
            books.pop(int(input("Book number to delete: ")) - 1)
            print("Book deleted.")
        except (ValueError, IndexError):
            print("Invalid book number.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
