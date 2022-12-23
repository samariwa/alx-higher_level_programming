#!/usr/bin/python3
"""
 Changes the name of the State object with id = 2 to
 New Mexico in the database hbtn_0e_6_usa.
 Usage: ./12-model_state_update_id_2.py <mysql username> /
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

    state_to_update = session.query(State).filter_by(id=2).first()
    state_to_update.name = 'New Mexico'
    session.commit()
