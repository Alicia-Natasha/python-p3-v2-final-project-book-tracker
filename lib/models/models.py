from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    loans = relationship("Loan", back_populates="user")

class Books(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    checked_out = Column(Boolean, default=False)
    loans = relationship("Loan", back_populates="book")
