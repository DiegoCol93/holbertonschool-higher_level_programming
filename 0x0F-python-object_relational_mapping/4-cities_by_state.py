#!/usr/bin/python3
''' Module for storing the 4. Cities by states task script. '''

if __name__ == "__main__":

    import MySQLdb
    from sys import argv as av

    args = {
        "host": "localhost",  # <-- Host Name.
        "port": 3306,  # <- - - --- Port Number.
        "user": av[1],  # <- - - -- User name.
        "passwd": av[2],  # <- - -- User password.
        "db": av[3],  # <- - - - -- Database name.
        "charset": "utf8"  # <- --- Character set.
    }

    # Create connection with database.
    with MySQLdb.connect(**args) as cursor:

        cmd = "SELECT cities.id, cities.name, states.name " \
              "FROM cities " \
              "LEFT JOIN states " \
              "ON cities.state_id = states.id " \
              "ORDER BY cities.id"

        cursor.execute(cmd)

        # Fetch all content and return it as tuple object.
        rows = cursor.fetchall()
        for row in rows:
            print(row)
