#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ints = 0
    while ints < x:
        try:
            print("{:d}".format(my_list[ints]), end='')
        except ValueError:
            pass
        ints += 1
    print()
    return ints
