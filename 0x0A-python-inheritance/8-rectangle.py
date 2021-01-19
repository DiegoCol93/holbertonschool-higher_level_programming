#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
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
