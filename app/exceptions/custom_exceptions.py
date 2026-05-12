class BookNotFound(Exception):
    """Raised when a book is not found in the database."""
    pass

class MemberNotFound(Exception):
    """Raised when a member is not found in the database."""
    pass

class BookNotAvailable(Exception):
    """Raised when a book is not available for borrowing."""
    pass

class BookNotBorrowed(Exception):
    """Raised when a member tries to return a book they haven't borrowed."""
    pass