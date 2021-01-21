#!/usr/bin/python3
""" Module for storing script to save argv[] as a text file and append. """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    the_list = load_from_json_file("add_item.json")
except:
    the_list = []
if len(sys.argv) > 1:
    the_list.extend(sys.argv[1:])
save_to_json_file(the_list, "add_item.json")
