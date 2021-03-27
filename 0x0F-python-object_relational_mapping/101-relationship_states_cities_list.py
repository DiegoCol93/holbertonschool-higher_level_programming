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

    # Create session cursor.
    session = Session(engine)

    # Create Query.
    args = [State.id, State.name, City.id, City.name]
    queryTable = session.query(*args).join(City)

    # Print on a specific format.
    state_num = 0
    for row in queryTable:
        if state_num == row[0]:
            print("    {}: {}".format(row[2], row[3]))
        else:
            print("{}: {}\n    {}: {}".format(row[0], row[1], row[2], row[3]))
            state_num = row[0]

    # Close session cursor.
    session.close()
