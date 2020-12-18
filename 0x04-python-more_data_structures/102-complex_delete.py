#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_t = list(a_dictionary.items())
    for i in list_t:
        if i[1] == value:
            del a_dictionary[i[0]]
    return a_dictionary
