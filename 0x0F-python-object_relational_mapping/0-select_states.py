#!/usr/bin/python3
''' Module for storing the 0. Get all states task script. '''

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

        # SELECT * FROM {databse}.
        cursor.execute("SELECT * FROM states")

        # Fetch all content and return it as tuple object.
        rows = cursor.fetchall()
        for row in rows:
            print(row)
