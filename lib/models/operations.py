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
            