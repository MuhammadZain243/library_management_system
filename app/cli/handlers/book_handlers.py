from app.services import Library
from app.models import Book

def handle_add_book(library: Library) -> None:
    library.add_book(
        Book(
            author=input("Enter author: "),
            title=input("Enter title: "),
            isbn=input("Enter ISBN: "),
            available=True,
            year=int(input("Enter year: "))
        )
    )

def handle_search_books(library: Library) -> None:
    title = input("Enter title to search (leave blank if not searching by title): ")
    author = input("Enter author to search (leave blank if not searching by author): ")
    results = library.search_book(title=title or None, author=author or None)
    
    for book in results:
        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.available}")

def handle_list_overdue_books(library: Library) -> None:
    overdue_books = library.list_overdue_books()
    for book in overdue_books:
        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Due Date: {book.due_date}")
