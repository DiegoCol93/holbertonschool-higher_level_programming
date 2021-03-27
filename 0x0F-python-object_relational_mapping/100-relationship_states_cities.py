#!/usr/bin/python3
''' Start link class to table in database '''

if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
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

    # Create a new City.
    cName = "San Francisco"
    newCity = City(name=cName)

    # Create new state.
    sName = "California"
    newState = State(name=sName, cities=[newCity])

    # Add the new state.
    session.add(newState)

    # Commit the change.
    session.commit()

    # Close session cursor.
    session.close()
