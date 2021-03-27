#!/usr/bin/python3
''' Start link class to table in database '''

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv as av
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import Session

    # Create engine connection. av[1]=Username av[2]=Password av[3]=DBName.
    engine = create_engine('mysql+mysqldb://' + '{}'.format(av[1]) +
                           ':{}'.format(av[2]) + '@localhost/' +
                           '{}'.format(av[3]), pool_pre_ping=True)

    # Creates all classes currently active.
    Base.metadata.create_all(engine)

    # Create session's cursor.
    session = Session(engine)

    # Create new state.
    sName = "Louisiana"
    newState = State(name=sName)

    # Add the new state.
    session.add(newState)

    # Print the new id.
    st = session.query(State).order_by(State.id).filter(State.name == sName)
    for state in st:
        print(state.id)

    # Commit the change.
    session.commit()

    # Close session cursor.
    session.close()
