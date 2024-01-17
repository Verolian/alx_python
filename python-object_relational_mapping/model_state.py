#!/usr/bin/python3
"""Defines the State class and Base instance."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the Base class
Base = declarative_base()

class State(Base):
    """State class."""
    __tablename__ = 'states'  # Link to the MySQL table 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Replace 'your_username', 'your_password', and 'hbtn_0e_0_usa' with your actual MySQL credentials
if __name__ == "__main__":
    from sys import argv

    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Extract command-line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database), pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)