from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    loans = relationship("Loan", back_populates="user")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    checked_out = Column(Boolean, default=False)
    loans = relationship("Loan", back_populates="book")

class Loan(Base):
    __tablename__ = 'loans'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    loan_date = Column(DateTime, default=datetime.datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")
