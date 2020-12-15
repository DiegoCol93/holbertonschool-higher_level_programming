#!/usr/bin/python3
def no_c(my_string):
    c_less = ''
    for i in my_string:
        if i != 'C' and i != 'c':
            c_less = c_less + i
    return c_less
