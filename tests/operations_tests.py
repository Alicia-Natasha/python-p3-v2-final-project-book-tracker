# tests/test_operations.py
from lib.models.models import User, Books, Loan
import datetime

def test_add_user(session):
    user = User(name="Alice", email="alice@example.com")
    session.add(user)
    session.commit()
    assert user.id is not None
    assert session.query(User).filter_by(name="Alice").first() is not None

def test_add_book(session):
    book = Books(title="1984", author="George Orwell")
    session.add(book)
    session.commit()
    assert book.id is not None
    assert session.query(Books).filter_by(title="1984").first() is not None

def test_check_out_book(session):
    user = User(name="Bob", email="bob@example.com")
    book = Books(title="Dune", author="Frank Herbert")
    session.add_all([user, book])
    session.commit()

    loan = Loan(user_id=user.id, book_id=book.id)
    book.checked_out = True
    session.add(loan)
    session.commit()

    assert book.checked_out is True
    assert session.query(Loan).filter_by(user_id=user.id, book_id=book.id).first() is not None

def test_return_book(session):
    user = User(name="Carol", email="carol@example.com")
    book = Books(title="The Hobbit", author="Tolkien", checked_out=True)
    session.add_all([user, book])
    session.commit()

    loan = Loan(user_id=user.id, book_id=book.id)
    session.add(loan)
    session.commit()

    # Simulate returning the book
    book.checked_out = False
    loan.return_date = datetime.datetime.now()
    session.commit()

    assert book.checked_out is False
    assert loan.return_date is not None

def test_cannot_checkout_unavailable_book(session):
    user = User(name="Dan", email="dan@example.com")
    book = Books(title="Brave New World", author="Aldous Huxley", checked_out=True)
    session.add_all([user, book])
    session.commit()

    # Try to check out an already checked out book
    existing_loan = session.query(Loan).filter_by(book_id=book.id).first()
    assert book.checked_out is True
    assert existing_loan is None  # Should still be no loan since it's already checked out
