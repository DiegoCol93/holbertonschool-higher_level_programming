#!/usr/bin/python3
""" Module for storing file writing function write_file(). """


def write_file(filename="", text=""):
    """ Function to write on a file.

        Args:
            filename (str): Name of the file to write in.
            text (str): Text to write into the file.
    """
    with open(filename, "w", encoding='utf-8') as the_file:
        return(the_file.write(text))
