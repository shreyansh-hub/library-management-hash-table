# main.py
# --------------------------------------------------
#  Library Management System - Main Program
# --------------------------------------------------

from hash_table import HashTable


def main():
    size = 10
    library = HashTable(size)

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Display All Books")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.insert_book(book_id, title, author)

        elif choice == 2:
            book_id = int(input("Enter Book ID to search: "))
            library.search_book(book_id)

        elif choice == 3:
            book_id = int(input("Enter Book ID to delete: "))
            library.delete_book(book_id)

        elif choice == 4:
            library.display_all()

        elif choice == 5:
            print("📌 Exiting Program...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
