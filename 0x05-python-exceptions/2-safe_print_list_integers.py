#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ints = 0
    for value in range(0, x):
        try:
            print("{:d}".format(my_list[value]), end='')
            ints += 1
        except (ValueError, TypeError):
            pass
    print()
    return ints
