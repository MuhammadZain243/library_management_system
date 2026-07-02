from app.services import Library
from app.models import Book, Member

def run_menu(library: Library) -> None:
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        switcher = {
            "1": lambda: handle_add_book(library),
            "2": library.add_member,
            "3": library.borrow_book,
            "4": library.return_book,
            "5": library.search_book,
            "6": library.list_overdue_books,
            "7": "export_books_to_csv",
            "8": exit
        }

        action = switcher.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

def handle_add_book(library: Library) -> None:
    book = Book(
        author=input("Enter author: "),
        title=input("Enter title: "),
        isbn=input("Enter ISBN: "),
        available=True,
        year=int(input("Enter year: "))
    )

    library.add_book(book)




def print_menu() -> None:
    print("""
          \nLibrary Management System Menu:
1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. Search Books
6. List Overdue Books
7. Export Books to CSV
8. Quit
    """)