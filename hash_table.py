# hash_table.py
# --------------------------------------
# Hash Table implementation for library
# --------------------------------------

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Chaining

    def hash_function(self, book_id):
        return book_id % self.size

    def insert_book(self, book_id, title, author):
        index = self.hash_function(book_id)

        # Check if book already exists
        for book in self.table[index]:
            if book[0] == book_id:
                print("❌ Book ID already exists!")
                return

        self.table[index].append([book_id, title, author])
        print("✅ Book added successfully!")

    def search_book(self, book_id):
        index = self.hash_function(book_id)

        for book in self.table[index]:
            if book[0] == book_id:
                print("\n📘 Book Found:")
                print(f"ID     : {book[0]}")
                print(f"Title  : {book[1]}")
                print(f"Author : {book[2]}")
                return

        print("❌ Book not found.")

    def delete_book(self, book_id):
        index = self.hash_function(book_id)

        for book in self.table[index]:
            if book[0] == book_id:
                self.table[index].remove(book)
                print("🗑️ Book deleted successfully!")
                return

        print("❌ Book not found.")

    def display_all(self):
        print("\n------ 📚 All Library Books -------")
        for i in range(self.size):
            print(f"Bucket {i}: {self.table[i]}")
        print("-----------------------------------")

