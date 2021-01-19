#!/usr/bin/python3
""" Module for storing an object comparison function. """


def inherits_from(obj, a_class):
    """ Returns if an object is a subclass of a_class or not """
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
