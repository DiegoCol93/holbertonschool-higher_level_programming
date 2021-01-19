#!/usr/bin/python3
"""
|    Module: For storing the BaseGeometry Class.    |
|    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨     |
|       _____   __  ______  ______  ______          |
|      /\  __-./\ \/\  ___\/\  ___\/\  __ \         |
|      \ \ \/\ \ \ \ \  __\  \ \__ \ \ \/\ \        |
|       \ \____-\ \_\ \_____\ \_____\ \_____\       |
|        \/____/ \/_/\/_____/\/_____/\/_____/       |
|      __      ______  ______  ______  ______       |
|     /\ \    /\  __ \/\  == \/\  ___\/\___  \      |
|     \ \ \___\ \ \/\ \ \  _-/\ \  __\ /_/  /__     |
|      \ \_____\ \_____\ \_\   \ \_____\/\_____\    |
|       \/_____/\/_____/\/_/    \/_____/\/_____/    |
|                                                   |
|                  | Jan-19-2021 |                  |
"""


# | Basegeometry | Super-Class |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
class BaseGeometry():
    """ BaseGeometry Parent Object Class """

    # | area | public | method | Un-implemented | . . . . . . . . . . . . . . .
    def area(self):
        """ Un-implemented method. """
        raise Exception("area() is not implemented")

    # | integer_validator | public | method | # # # # # # # # # # # # # # # # #
    def integer_validator(self, name, value):
        """ integer_validator method, for the value argument. """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
