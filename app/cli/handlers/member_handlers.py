from app.services import Library
from app.models import Member

def handle_add_member(library: Library) -> None:
    library.add_member(
        Member(
            id=input("Enter member ID: "),
            name=input("Enter member name: ")
        )
    )