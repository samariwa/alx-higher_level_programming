#!/usr/bin/python3
"""
 Prints the first State object from the database hbtn_0e_6_usa.
 Usage: ./8-model_state_fetch_first.py <mysql username> 
                                       <mysql password>
                                       <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).first()
    print("{}: {}".format(result.id, result.name))
