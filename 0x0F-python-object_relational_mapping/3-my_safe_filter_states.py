#!/usr/bin/python3
''' Module for storing the 3. SQL Injection... task script. '''

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

    parsed = ''
    if len(av) == 5:
        # Ask av[4] has a ';' in it.
        if av[4].count(';') != 0:
            # # Print the incoming attack attempt.
            # red = "\033[91m"
            # reset = "\033[m"
            # print(red + av[4] + reset)
            # attack = av[4].split(';', 1)  # Split at ';' character.
            parsed = ''
        else:
            # Set argument to be parsed.
            parsed = av[4]

    # Clean newlines, and quotes.
    parsed = parsed.replace("\n", '')
    parsed = parsed.replace("'", '')
    parsed = parsed.replace('"', "")

    # Create connection with database.
    with MySQLdb.connect(**args) as cursor:

        # SELECT * WHERE name matches the given argument.
        cursor.execute("SELECT * FROM states WHERE name='{}'".format(parsed))

        # Fetch all content and return it as tuple object.
        rows = cursor.fetchall()
        for row in rows:
            print(row)
