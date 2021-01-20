#!/usr/bin/python3
""" Module 0-read_file """


def read_file(filename=""):
    """ Function for reading a file.

        Args:
            filename (str): Name of the file to read from.
    """
    with open("{}".format(filename),"r", encoding='utf-8') as the_file:
        print(the_file.read(), end='')
