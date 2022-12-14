#!/usr/bin/python3
"""
 Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
 Usage: ./11-model_state_insert.py <mysql username> /
                                   <mysql password> /
                                   <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # establish connection to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_add = State(name='Louisiana')
    session.add(state_to_add)
    session.commit()
