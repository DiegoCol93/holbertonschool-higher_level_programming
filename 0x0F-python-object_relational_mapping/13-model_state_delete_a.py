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

    # Get the State of id 2.
    st = session.query(State).filter(State.name.like('%a%'))

    for state in st:
        session.delete(state)

    # Commit the change.
    session.commit()

    # Close session cursor.
    session.close()
