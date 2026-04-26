# 📚 Library Management System using Hash Table

[cite_start]A high-performance Library Management System implemented in Python that leverages a custom **Hash Table** data structure to ensure efficient book record management and near-instant retrieval[cite: 1, 4].

---

## 🚀 Overview
[cite_start]Traditional list-based storage systems suffer from linear search times because they require checking each book one-by-one[cite: 11]. [cite_start]This project solves that problem by implementing a custom Hash Table, reducing search and insertion time complexity from $O(n)$ to an average of **$O(1)$**[cite: 11, 35].

## ✨ Features
* [cite_start]**Add Book**: Create new records with a unique Book ID, Title, and Author[cite: 14, 16].
* [cite_start]**Search Book**: Retrieve book details instantly using the Book ID[cite: 14, 18].
* [cite_start]**Remove Book**: Delete existing records from the system[cite: 14, 17].
* [cite_start]**View All**: Display all buckets and the books stored within them[cite: 20].
* [cite_start]**Collision Handling**: Uses **Chaining** to manage multiple books mapping to the same index[cite: 14, 24].
* [cite_start]**Data Persistence**: Uses file handling to ensure data is saved and loaded across sessions[cite: 35, 57].

## 🛠 Tech Stack
* **Language**: Python 3.x
* [cite_start]**Core Concepts**: Object-Oriented Programming (OOP) and Data Structures [cite: 32, 33]
* [cite_start]**Storage**: File Handling for permanent data records [cite: 31, 57]

## 🧠 How It Works
1.  [cite_start]**Hash Function**: The system takes the `book_id` and passes it through a hash function: `book_id % table_size`[cite: 24, 42].
2.  [cite_start]**Indexing**: The function generates an index where the book is stored inside a list[cite: 24].
3.  [cite_start]**Collision Resolution**: If two different keys generate the same index (a collision), they are stored in the same "bucket" using a linked list or Python list (Chaining)[cite: 24, 48].



## 📊 Time Complexity
| Operation | Average Case | Worst Case |
| :--- | :--- | :--- |
| **Insertion** | [cite_start]$O(1)$ [cite: 51] | [cite_start]$O(n)$ [cite: 51] |
| **Search** | [cite_start]$O(1)$ [cite: 51] | [cite_start]$O(n)$ [cite: 51] |
| **Deletion** | [cite_start]$O(1)$ [cite: 51] | [cite_start]$O(n)$ [cite: 51] |

## ⚙️ Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/shreyansh-hub/library-management-hash-table.git](https://github.com/shreyansh-hub/library-management-hash-table.git)
   cd library-management-hash-table
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

---
**Author**: Shreyansh Mishra
```
* [cite_start]**Why Hashing?** It provides near-instant access compared to arrays or lists which require slow linear searches[cite: 39, 54].
* [cite_start]**Scalability:** The system remains efficient even with large datasets (e.g., 1 million books) as long as the load factor is controlled[cite: 64, 66].
* [cite_start]**Challenges Faced:** Managing collisions effectively and ensuring data integrity during file loading were the primary technical hurdles[cite: 58, 60].
