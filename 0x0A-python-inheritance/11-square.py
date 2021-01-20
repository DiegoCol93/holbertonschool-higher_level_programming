#!/usr/bin/python3
"""
|     Module: For storing the Rectangle Class.      |
|     ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨      |
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
Rectangle = __import__('9-rectangle').Rectangle


# | Square | Sub-Class  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
class Square(Rectangle):
    """ Square class, inherits from Rectangle """

    # | __init__ | private | method | # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, size):
        """ __init__ :

            Args:
                size (int): Value for the Square object
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    # | area | public | method | override | # # # # # # # # # # # # # # # # # #
    def area(self):
        return super().area()

    # | __str__ | private | method |  # # # # # # # # # # # # # # # # # # # # #
    def __str__(self):
        return("[Square] {}/{}".format(self.__size, self.__size))
