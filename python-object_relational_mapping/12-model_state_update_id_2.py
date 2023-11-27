#!/usr/bin/python3
"""
    a script that changes the name of a State object from the database
    hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state id>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_id = sys.argv[1:5]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == state_id).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()
