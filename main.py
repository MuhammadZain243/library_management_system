from app.cli import run_menu
from app.services import load_library


def main() -> None:
    library = load_library()
    run_menu(library)

if __name__ == "__main__":
    main()