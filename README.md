# Library Management System

A command-line based Library Management System built with Python using Object-Oriented Programming principles.

This project demonstrates:

- Clean class design
- File persistence with JSON
- Custom exceptions
- Type hints
- Logging decorators
- CSV export
- Overdue tracking and late fee calculation

---

## Features

### Core Features

- Add books
- Add members
- Borrow books
- Return books
- Search books
- Persistent storage using JSON
- CLI menu system

### Stretch Features

- Borrow and due date tracking
- Overdue book detection
- Late fee calculation using `Decimal`
- CSV export
- Operation logging with decorators

---

## Project Structure

```text
library_management_system/
│
├── app/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py
│   │   ├── member.py
│   │   └── loan.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── library.py
│   │   ├── persistence.py
│   │   └── export_service.py
│   │
│   ├── exceptions/
│   │   ├── __init__.py
│   │   └── custom_exceptions.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   ├── fee_calculator.py
│   │   └── helpers.py
│   │
│   └── cli/
│       ├── __init__.py
│       └── menu.py
│
├── data/
│   ├── library.json
│   ├── books.csv
│   └── operations.log
│
├── tests/
│   ├── __init__.py
│   ├── test_book.py
│   ├── test_member.py
│   └── test_library.py
│
├── venv/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

- Python 3.10+
- pip

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd library_management_system
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## CLI Menu

```text
1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. Search Books
6. List Overdue Books
7. Export Books to CSV
8. Quit
```

---

## Technologies Used

- Python
- JSON
- CSV
- `datetime`
- `decimal`
- `dataclasses`
- `pathlib`

---

## Functional Requirements

### `Book` Class

Contains:

| Field     | Type |
| --------- | ---- |
| title     | str  |
| author    | str  |
| isbn      | str  |
| year      | int  |
| available | bool |

Optional:

| Field       | Type     |
| ----------- | -------- |
| borrow_date | datetime |
| due_date    | datetime |

### `Member` Class

Contains:

| Field          | Type      |
| -------------- | --------- |
| id             | str       |
| name           | str       |
| email          | str       |
| borrowed_books | list[str] |

### `Library` Class

Provides methods:

- `add_book()`
- `add_member()`
- `borrow()`
- `return_book()`
- `search()`
- `list_overdue()`

---

## Persistence

- Data stored in `library.json`
- Auto-save on every change
- Auto-load on startup

---

## Exception Handling

Custom exceptions:

- `BookNotFound`
- `MemberNotFound`
- `BookNotAvailable`

---

## Additional Features

### Late Fees

- Uses `Decimal`
- Fee: **$0.50 per overdue day**

### CSV Export

Exports all books using Python's `csv` module.

### Logging Decorator

Logs all operations to `data/operations.log`.

---

## Coding Standards

- No global variables
- Type hints on every function
- Public methods contain docstrings
- Methods kept under 20 lines
- Modular architecture
- Uses `with` for all file operations

---

## Example: Search Feature

Search by author uses dictionary comprehension:

```python
{
    isbn: book
    for isbn, book in self.books.items()
    if author.lower() in book.author.lower()
}
```

---

## Future Improvements

- SQLite integration
- GUI version using Tkinter/PyQt
- REST API using Flask/FastAPI
- Authentication system
- Advanced analytics dashboard

---

## Testing

Run tests using:

```bash
python -m unittest discover tests
```
