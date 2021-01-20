#!/usr/bin/python3
""" Module for storing append file writing function. """


def append_write(filename="", text=""):
    """ Function for appending to a file.

        Args:
            filename (str): Name of the file to append to.
            text (str): Text to append to the file.
    """
    with open(filename, "a", encoding='utf-8') as the_file:
        return(the_file.write(text))
