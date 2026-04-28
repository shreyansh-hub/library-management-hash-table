# Library Management System

A simple command-line Library Management System built in Python, using a custom **Hash Table** data structure with chaining for efficient book storage and retrieval.

---

## Project Structure

```
├── hash_table.py   # Hash Table implementation (core data structure)
├── main.py         # Entry point — CLI menu and user interaction
└── README.md       # Project documentation
```

---

## How It Works

The system uses a **Hash Table with separate chaining** to manage books:

- Each book is stored as `[book_id, title, author]` in a bucket.
- The bucket index is determined by: `book_id % table_size`
- Collisions are resolved via **chaining** (each bucket holds a list of books).

### Hash Function

```python
def hash_function(self, book_id):
    return book_id % self.size
```

---

## Getting Started

### Prerequisites

- Python 3.x

### Run the Program

```bash
python main.py
```

---

## Usage

On launch, you'll see an interactive menu:

```
===== Library Menu =====
1. Add Book
2. Search Book
3. Delete Book
4. Display All Books
5. Exit
```

| Option | Description                          |
|--------|--------------------------------------|
| 1      | Add a new book (ID, Title, Author)   |
| 2      | Search for a book by its ID          |
| 3      | Delete a book by its ID              |
| 4      | Display all books across all buckets |
| 5      | Exit the program                     |

---

## Example

```
Enter choice: 1
Enter Book ID: 101
Enter Book Title: The Pragmatic Programmer
Enter Author Name: Andy Hunt
Book added successfully!

Enter choice: 2
Enter Book ID to search: 101

Book Found:
ID     : 101
Title  : The Pragmatic Programmer
Author : Andy Hunt
```

---

## Time Complexity

| Operation | Average Case | Worst Case (all collisions) |
|-----------|--------------|-----------------------------|
| Insert    | O(1)         | O(n)                        |
| Search    | O(1)         | O(n)                        |
| Delete    | O(1)         | O(n)                        |

---

## Classes & Methods

### `HashTable` (`hash_table.py`)

| Method | Description |
|---|---|
| `__init__(size)` | Initializes the hash table with `size` buckets |
| `hash_function(book_id)` | Computes the bucket index for a given book ID |
| `insert_book(book_id, title, author)` | Inserts a new book; rejects duplicate IDs |
| `search_book(book_id)` | Searches and prints book details by ID |
| `delete_book(book_id)` | Removes a book by ID |
| `display_all()` | Prints all buckets and their contents |

---

## Possible Improvements

- Persist data to a file (JSON/CSV) so books survive between sessions
- Support updating book details after insertion
- Add sorting/filtering when displaying all books
- Implement dynamic resizing when the load factor exceeds a threshold

---

## License

This project is open-source and free to use for educational purposes.
