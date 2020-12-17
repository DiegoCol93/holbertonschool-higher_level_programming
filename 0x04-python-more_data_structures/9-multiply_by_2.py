#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_new_dictionary = a_dictionary.copy()
    for value in a_dictionary:
        a_new_dictionary[value] *= 2
    return(a_new_dictionary)
