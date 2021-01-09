#!/usr/bin/python3
""" Name printing module with a formatted function """


def say_my_name(first_name, last_name=""):
    """ Prints a name using format "My name is <first name> <last name>"

        Args:
            first_name (str): Fisrt name
            last_name (str): Last name

        Raises
            TypeError: if name not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
