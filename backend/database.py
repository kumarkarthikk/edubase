"""
database.py
------------
This file sets up the connection to our SQLite database.
SQLite stores everything in a single file (edubase.db) — no server needed.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The database file will be created automatically in the backend folder
DATABASE_URL = "sqlite:///./edubase.db"

# engine = the actual connection to the database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed only for SQLite
)

# SessionLocal = used to talk to the database (insert, update, query)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = all our table classes (in models.py) will inherit from this
Base = declarative_base()


def get_db():
    """
    This function gives a database session to each API request,
    and closes it automatically once the request is done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()