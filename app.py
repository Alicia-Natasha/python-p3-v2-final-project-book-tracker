from database import Base, engine
from cli import list_books, add_book, borrow_book, return_book

def main():
    Base.metadata.create_all(engine)
    
    while True:
        print("\nLibrary Book Tracker")
        print("1. List all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
