import json
from pathlib import Path
from datetime import datetime
from app.models import Book, Member
from app.services.library import Library

def save_library(library: Library) -> None:
    """Saves the library state to a JSON file."""

    data = {
        "books": {
            isbn: {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "year": book.year,
                "available": book.available,
                "borrow_date":book.borrow_date.isoformat() if book.borrow_date else None,
                "due_date": book.due_date.isoformat() if book.due_date else None,
            }
            for isbn, book in library.books.items()
        },
        "members": {
            member_id:{
                "id": member.id,
                "name": member.name,
                "email": member.email,
                "borrowed_books": member.borrowed_books,
            }
            for member_id, member in library.members.items()
        }
    }
    
    Path("data").mkdir(exist_ok=True)
    with open("data/library.json", "w") as f:
        json.dump(data, f, indent=4)

def load_library() -> Library:
    """Loads the library state from a JSON file."""

    path = Path("data/library.json")
    if not path.exists():
        return Library() # Return an empty library if no data file exists
    
    with open(path, "r") as f:
        data = json.load(f)
        library = Library()

        for isbn, book_data in data["books"].items():
            book = Book(
                title= book_data["title"],
                author= book_data["author"],
                isbn= isbn,
                year= book_data["year"],
                available= book_data["available"],
                borrow_date= datetime.fromisoformat(book_data["borrow_date"]) if book_data["borrow_date"] else None,
                due_date= datetime.fromisoformat(book_data["due_date"]) if book_data["due_date"] else None,
           )
            library.add_book(book)
        
        for member_id, member_data in data["members"].items():
            member = Member(
                id= member_id,
                name= member_data["name"],
                email= member_data["email"],
            )
            member.borrowed_books = member_data["borrowed_books"]
            library.add_member(member)

    return library