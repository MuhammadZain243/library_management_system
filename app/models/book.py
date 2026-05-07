from datetime import datetime

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title: str, author: str, isbn: str, year: int, available: bool = True, borrow_date: datetime | None = None, due_date: datetime | None = None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = available
        self.borrow_date = borrow_date
        self.due_date = due_date
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Year: {self.year}) - {'Available' if self.available else 'Checked out'}"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', year={self.year}, available={self.available}, borrow_date={self.borrow_date}, due_date={self.due_date})"
        