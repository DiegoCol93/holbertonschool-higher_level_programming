#!/usr/bin/python3
""" Module for storing the from_json_string function. """
import json


def from_json_string(my_str):
    """ Turns a JSON formatted text into a string. """
    return json.loads(my_str)
