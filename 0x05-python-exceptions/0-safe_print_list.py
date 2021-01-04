#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item = 0
    while item < x:
        try:
            print("{}".format(my_list[item]), end='')
        except:
            break
        item += 1
    print()
    return(item)
