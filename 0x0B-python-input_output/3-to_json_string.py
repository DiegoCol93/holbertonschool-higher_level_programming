#!/usr/bin/python3
""" Module for storing dict to json function. """
import json


def to_json_string(my_obj):
    """ Funtion that turns a string of chars into json format. """
    return json.dumps(my_obj)
