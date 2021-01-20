#!/usr/bin/python3
"""Module that defines a function that adds an attribute"""


def add_attribute(object, name, value):
    """Method that add a new attribute to the object.
    Args:
       name: A new attribute.
       value: Value to assign to the attribute.
    Return:
       Always nothing
    """
    if hasattr(object, "__dict__") is not True:
            raise TypeError("can't add new attribute")
    else:
        object.__setattr__(name, value)"'")
