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

    # Parse the user-given argument.
    parsed = ''
    try:  # Check if bad argument was passed.
        if av[4].count(';') != 0:
            # # Print the incoming attack attempt.
            # red = "\033[91m"
            # reset = "\033[m"
            # print(red + av[4] + reset)
            attack = av[4].split(';', 1)  # Split at ';' character.
            parsed = attack[0]
        else:
            parsed = av[4]
        parsed = parsed.replace("\n", '')
        parsed = parsed.replace("'", '')
        parsed = parsed.replace('"', "")
    except:
        pass

    try:
        # Create connection with database.
        with MySQLdb.connect(**args) as cursor:

            cmd = "SELECT cities.name " \
                  "FROM cities " \
                  "LEFT JOIN states " \
                  "ON cities.state_id = states.id " \
                  "WHERE states.name = '{}';".format(parsed)

            cursor.execute(cmd)

            # Fetch all content and return it as tuple object.
            rows = cursor.fetchall()

            # Print on a specific format "City0, City1, ..."
            for i in range(len(rows)):
                if i != len(rows) - 1:
                    print("{}, ".format(rows[i][0]), end='')
                else:
                    print("{}".format(rows[i][0]), end='')
            print()
    except:
        print()
