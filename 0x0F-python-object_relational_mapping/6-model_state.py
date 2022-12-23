#!/usr/bin/python3
"""
Start link class to table in database
Usage: ./6-model_state.py <mysql username>
                                     <mysql password>
                                     <database name>
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # establish connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
