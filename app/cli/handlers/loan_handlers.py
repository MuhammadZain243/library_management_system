from app.services import Library

def handle_borrow_book(library: Library) -> None:
    library.borrow_book(
        member_id=input("Enter member ID: "),
        isbn=input("Enter ISBN of the book to borrow: ")
    )


def handle_return_book(library: Library) -> None:
    library.return_book(
        member_id=input("Enter member ID: "),
        isbn=input("Enter ISBN of the book to return: ")
    )