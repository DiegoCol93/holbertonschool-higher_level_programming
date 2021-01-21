#!/usr/bin/python3
""" Module for storing class_to_json function. """


def class_to_json(obj):
    """ Returns the dictionary description. """
    return dict(obj.__dict__)
