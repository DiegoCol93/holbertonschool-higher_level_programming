#!/usr/bin/python3
""" Module for storing the save_to_jason_file """
import json


def save_to_json_file(my_obj, filename):
    """ Saves an Object as JSON string format into a text file.  """
    with open(filename, "w") as json_txt_file:
        json_txt_file.write(json.dumps(my_obj))
