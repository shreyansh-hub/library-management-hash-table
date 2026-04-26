# Library Management System using Hash Table (Python)

## Overview

This is a simple Library Management System implemented in Python. It uses a **custom hash table** to store book records efficiently. The system allows adding, searching, deleting, updating, and displaying books. Data is persisted using file handling.

## Features

- Add new books with Book ID, Title, and Author
- Search books by Book ID
- Delete books
- View all books
- Collision handling using chaining
- Fast lookup using hashing
- File storage for persistent data

## Data Structure

- Hash Table with Chaining
- Hash Function: `book_id % table_size`
- Each index contains a list to handle collisions

## Tech Stack

- Python 3.x
- Object-Oriented Programming (OOP)
- File Handling

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/yourusername/library-hash-table.git
```

Navigate to project folder:


cd library-hash-table



Run the program:


python main.py

Example Output
===== Library Menu =====
1. Add Book
2. Search Book
3. Delete Book
4. Display All Books
5. Exit

Learning Outcomes


Understanding and implementation of hash tables


Collision handling using chaining


Practical OOP in Python


File handling for persistent data storage



---
