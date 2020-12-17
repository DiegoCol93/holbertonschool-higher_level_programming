#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_new_dictionary = a_dictionary.copy()
    a_new_dictionary[key] = value
    return(a_new_dictionary)
