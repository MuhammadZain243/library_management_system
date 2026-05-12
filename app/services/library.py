from app.models import Book, Member
from app.exceptions import BookNotFound, BookNotAvailable, MemberNotFound, BookNotBorrowed
from datetime import datetime, timedelta

class Library:
    """Manages books and members in the library."""

    def __init__(self):
        self.books : dict[str, Book] = {}
        self.members : dict[str, Member] = {}
    
    def add_book(self, book: Book):
        self.books[book.isbn] = book
    
    def add_member(self, member: Member):
        self.members[member.id] = member
    
    def borrow(self, member_id: str, isbn: str):
        """Allows a member to borrow a book if it's available."""
        # check member exists
        if member_id not in self.members:
            raise MemberNotFound(f"Member with ID {member_id} not found.")
        
        # check book exists
        if isbn not in self.books:
            raise BookNotFound(f"Book with ISBN {isbn} not found.")
        
        # check book availability
        if not self.books[isbn].available:
            raise BookNotAvailable(f"Book with ISBN {isbn} is not available for borrowing.")
        
        # borrow the book
        self.books[isbn].available = False
        self.members[member_id].borrowed_books.append(isbn)
        self.books[isbn].borrow_date = datetime.now()
        self.books[isbn].due_date = self.books[isbn].borrow_date + timedelta(days=14)  # 2 weeks loan period
    
    def return_book(self, member_id: str, isbn: str):
        """Allows a member to return a borrowed book."""
        # check member exists
        if member_id not in self.members:
            raise MemberNotFound(f"Member with ID {member_id} not found.")
        
        # check book exists
        if isbn not in self.books:
            raise BookNotFound(f"Book with ISBN {isbn} not found.")
        
        # check if member has borrowed that book
        if isbn not in self.members[member_id].borrowed_books:
            raise BookNotBorrowed(f"Member with ID {member_id} has not borrowed book with ISBN {isbn}.")
        
        # return the book
        self.books[isbn].available = True
        self.members[member_id].borrowed_books.remove(isbn)
        self.books[isbn].borrow_date = None
        self.books[isbn].due_date = None
    
    def search(self, title: str | None = None, author: str | None = None) -> list[Book]:
        """Searches for books by title and/or author."""
        return [
            book for book in self.books.values()
            if (title and title.lower() in book.title.lower())
            or (author and author.lower() in book.author.lower())
        ]
    
    def list_overdue(self) -> list[Book]:
        """Lists all overdue books."""
        now = datetime.now()
        return [
            book for book in self.books.values()
            if not book.available and book.due_date and book.due_date < now
        ]