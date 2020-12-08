#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if ord(i) > 96 and ord(i) < 123:
            c -= 32
        print("{:c}".format(c), end='')
    print()
