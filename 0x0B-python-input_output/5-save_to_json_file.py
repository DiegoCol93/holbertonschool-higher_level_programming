#!/usr/bin/python3
"""  """
import json


def save_to_json_file(my_obj, filename):
    """  """
    with open(filename, "w") as json_txt_file:
        json_txt_file.write(json.dumps(my_obj))
