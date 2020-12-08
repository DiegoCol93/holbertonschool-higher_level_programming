#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str_num = str(number)
last_digit = int(str(number)[-1:])

print("Last digit of {0:d} is".format(number), end=' ')
if number > 0 and str_num[-1:] != '0':
    print("{0:s}".format(str_num[-1:]), end=' ')
if last_digit == 0:
    print("0", end=' ')
if number < 0 and str_num[-1:] != '0':
    print("-{0:s}".format(str_num[-1:]), end=' ')

if last_digit > 5 and number > 0:
    print("and is greater than 5")
if last_digit == 0:
    print("and is 0")
elif number < 0 and last_digit != 0 or last_digit < 6:
    print("and is less than 6 and not 0")
