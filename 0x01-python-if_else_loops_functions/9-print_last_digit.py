#!/usr/bin/python3
def print_last_digit(number):
    temp = str(abs(number))
    print("{:s}".format(temp[-1:]), end='')
    return int(temp[-1:])
