#!/usr/bin/python3
def print_last_digit(number):
    temp = str(number)
    print("{:s}".format(temp[-1:]), end='')
    return temp[-1:]
