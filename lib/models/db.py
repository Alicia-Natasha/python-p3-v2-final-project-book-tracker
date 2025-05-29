from sqlalchemy import create_engine
from models import Base

# Create an SQLite database
engine = create_engine("sqlite:///data/library.db")

# Create all tables based on models
Base.metadata.create_all(engine)
