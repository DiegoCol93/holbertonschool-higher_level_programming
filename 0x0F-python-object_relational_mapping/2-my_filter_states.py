#!/usr/bin/python3
''' Module for storing the 2. Filter states by user input task script. '''

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

        # SELECT * WHERE name matches the given argument.
        cursor.execute("SELECT * FROM states WHERE name='{}'".format(av[4]))

        # Fetch all content and return it as tuple object.
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == av[4]:
                print(row)
