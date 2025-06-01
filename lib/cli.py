from models.models import User, Book, Loan
from sqlalchemy.orm import Session
from lib.db import engine, Base
import datetime

class CLI:
    def __init__(self):
        self.session = Session(engine)

    def run(self):
        while True:
            print("\n--- Library Book Tracker ---")
            print("1. Manage Users")
            print("2. Manage Books")
            print("3. Manage Loans")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.user_menu()
            elif choice == "2":
                self.book_menu()
            elif choice == "3":
                self.loan_menu()
            elif choice == "4":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. Create User")
            print("2. Delete User")
            print("3. List All Users")
            print("4. Find User by ID")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == "1":
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                user = User(name=name, email=email)
                self.session.add(user)
                self.session.commit()
                print(f"User created with ID: {user.id}")
            elif choice == "2":
                id = input("Enter user ID to delete: ")
                user = self.session.query(User).get(id)
                if user:
                    self.session.delete(user)
                    self.session.commit()
                    print("User deleted.")
                else:
                    print("User not found.")
            elif choice == "3":
                users = self.session.query(User).all()
                for u in users:
                    print(f"ID: {u.id}, Name: {u.name}, Email: {u.email}")
            elif choice == "4":
                id = input("Enter user ID: ")
                user = self.session.query(User).get(id)
                if user:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
                    for loan in user.loans:
                        print(f"Loaned Book ID: {loan.book_id}, Loan Date: {loan.loan_date}, Return Date: {loan.return_date}")
                else:
                    print("User not found.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def book_menu(self):
        while True:
            print("\n--- Book Menu ---")
            print("1. Add Book")
            print("2. Delete Book")
            print("3. List All Books")
            print("4. Find Book by ID")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(title=title, author=author)
                self.session.add(book)
                self.session.commit()
                print(f"Book added with ID: {book.id}")
            elif choice == "2":
                id = input("Enter book ID to delete: ")
                book = self.session.query(Book).get(id)
                if book:
                    self.session.delete(book)
                    self.session.commit()
                    print("Book deleted.")
                else:
                    print("Book not found.")
            elif choice == "3":
                books = self.session.query(Book).all()
                for b in books:
                    status = "Checked Out" if b.checked_out else "Available"
                    print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}, Status: {status}")
            elif choice == "4":
                id = input("Enter book ID: ")
                book = self.session.query(Book).get(id)
                if book:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Status: {'Checked Out' if book.checked_out else 'Available'}")
                    for loan in book.loans:
                        print(f"Loaned to User ID: {loan.user_id}, Loan Date: {loan.loan_date}, Return Date: {loan.return_date}")
                else:
                    print("Book not found.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def loan_menu(self):
        while True:
            print("\n--- Loan Menu ---")
            print("1. Check Out Book")
            print("2. Return Book")
            print("3. List All Loans")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == "1":
                user_id = input("Enter user ID: ")
                book_id = input("Enter book ID: ")
                user = self.session.query(User).get(user_id)
                book = self.session.query(Book).get(book_id)
                if user and book and not book.checked_out:
                    loan = Loan(user_id=user.id, book_id=book.id)
                    book.checked_out = True
                    self.session.add(loan)
                    self.session.commit()
                    print(f"Book '{book.title}' checked out to {user.name}.")
                else:
                    print("Invalid user/book or book is already checked out.")
            elif choice == "2":
                book_id = input("Enter book ID to return: ")
                loan = self.session.query(Loan).filter_by(book_id=book_id, return_date=None).first()
                book = self.session.query(Book).get(book_id)
                if loan and book:
                    loan.return_date = datetime.datetime.now()
                    book.checked_out = False
                    self.session.commit()
                    print("Book returned.")
                else:
                    print("No active loan found for this book.")
            elif choice == "3":
                loans = self.session.query(Loan).all()
                for l in loans:
                    print(f"Loan ID: {l.id}, User ID: {l.user_id}, Book ID: {l.book_id}, Loan Date: {l.loan_date}, Return Date: {l.return_date}")
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Create tables if they don't exist
    CLI().run()
