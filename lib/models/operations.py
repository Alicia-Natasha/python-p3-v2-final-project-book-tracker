from models import User
from models import Books
from models import Loan
from sqlalchemy.orm import Session
from db import engine
import datetime

class Operations:

    def add_user(name):
        """Add a new user to the database."""
        with Session(engine) as session:
            new_user = User(name=name)
            session.add(new_user)
            session.commit()
            print(f"User {name} added with ID {new_user.id}")

    def add_book(title, author):
        with Session(engine) as session:
            """Add a new book to the database."""
            new_book = Books(title=title, author=author)
            session.add(new_book)
            session.commit()
            print(f"Book '{title}' by {author} added with ID {new_book.id}")

    def check_out_book(user_id, book_title):
        """Check out a book for a user."""
        with Session(engine) as session:
            book = session.query(Books).filter_by(Books.id == book_title, is_checked_out=False).first()
            if not book or book.checked_out:
                print(f"Book {book_title} is not available for checkout.")
                return
            
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                print(f"User {user_id} does not exist.")
                return
            
            new_loan = Loan(user_id=user.id, book_title=book.title)
            book.checked_out = True
            session.add(new_loan)
            session.commit()
            print(f"Book '{book.title}' checked out to User ID {user.id}.")

    def return_book(user_id, book_title):
        """Return a book for a user."""
        with Session(engine) as session:
            book = session.query(Books).filter_by(title=book_title, is_checked_out=True).first()
            if not book:
                print(f"No active loan found for User ID {user_id} and Book '{book_title}'.")
                return
            
            book.checked_out = False
            book.return_date = datetime.datetime.now()
            session.commit()
            print(f"Book '{book.title}' returned by User ID {user_id}.")    

    def search_books_by_title(title):
        """Search for books by title."""
        with Session(engine) as session:
            books = session.query(Books).filter(Books.title.ilike(f"%{title}%")).all()
            if not books:
                print(f"No books found with title containing '{title}'.")
                return
            
            for book in books:
                status = "Available" if not book.checked_out else "Checked Out"
                print(f"Found Book: {book.title} by {book.author} (ID: {book.id})")

    def search_books_by_author(author):
        """Search for books by author."""
        with Session(engine) as session:
            books = session.query(Books).filter(Books.author.ilike(f"%{author}%")).all()
            if not books:
                print(f"No books found by author '{author}'.")
                return
            
            for book in books:
                status = "Available" if not book.checked_out else "Checked Out"
                print(f"Found Book: {book.title} by {book.author} (ID: {book.id})")

    def list_all_books():
        """List all books in the library."""
        with Session(engine) as session:
            books = session.query(Books).all()
            if not books:
                print("No books found in the library.")
                return
            
            for book in books:
                status = "Available" if not book.checked_out else "Checked Out"
                print(f"Book: {book.title} by {book.author} (ID: {book.id}) - {status}")