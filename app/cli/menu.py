from app.cli.handlers import handle_search_books, handle_add_book, handle_list_overdue_books, handle_add_member, handle_return_book, handle_borrow_book
from app.cli.display import print_menu
from app.services import Library

def run_menu(library: Library) -> None:
    actions = {
        "1": handle_add_book,
        "2": handle_search_books,
        "3": handle_list_overdue_books,
        "4": handle_add_member,
        "5": handle_borrow_book,
        "6": handle_return_book,
    }

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("Exiting the Library Management System. Goodbye!")
            return
        
        action = actions.get(choice)

        if action is None:
            print("Invalid choice. Please try again.")
            continue

        action(library)