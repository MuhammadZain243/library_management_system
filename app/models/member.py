class Member:
    """Represents a library member."""

    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books: list[str] = []
    
    def __str__(self):
        return f"{self.name} (ID: {self.id}, Email: {self.email})"
    
    def __repr__(self):
        return f"Member(id='{self.id}', name='{self.name}', email='{self.email}', borrowed_books={self.borrowed_books})"