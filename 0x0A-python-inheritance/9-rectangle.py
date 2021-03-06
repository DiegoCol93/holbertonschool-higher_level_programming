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
BaseGeometry = __import__('7-base_geometry').BaseGeometry


# | Rectangle | Sub-Class |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
class Rectangle(BaseGeometry):
    """ Rectangle class, inherits from BaseGeometry """

    # | __init__ | private | method | # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, width, height):
        """ __init__ :

            Args:
                width (int): Private width value for Rectangle
                height (int): Private height value for Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    # | area | public | method | override | # # # # # # # # # # # # # # # # # #
    def area(self):
        return self.__width * self.__height

    # | __str__ | private | method |  # # # # # # # # # # # # # # # # # # # # #
    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
