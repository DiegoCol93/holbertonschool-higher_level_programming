#!/usr/bin/python3
""" Module for storing object comparison function. """


def is_same_class(obj, a_class):
    """ Returns if an object is or not the same class. """
    return type(obj) is a_class
