#!/usr/bin/python3
""" Module for storing Student class. """


class Student():
    """ Studen class, with age, first and last name. """
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """ __init__ :

            Args:
                first_name(str): Student's first_name
                last_name(str): Student's last_name
                age(str): Student's age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary representation of a Student instance

            Returns:
                dictionary representation of the Student
        """
        if type(attrs) is list:
            new_dict = {}
            for key in attrs:
                try:
                    new_dict[key] = self.__dict__[key]
                except KeyError:
                    pass
            return new_dict
        else:
            return self.__dict__
