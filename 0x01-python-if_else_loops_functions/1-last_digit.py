#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# If number negative, get negative last digit.
if number < 0:
    digit = ((number % 10) * -1)
else:
    digit = number % 10

# Begin Printing.
print("Last digit of {} is {} and is".format(number, digit), end=' ')

# Conditional printing.
if digit > 5:
    print("greater than 5")
if digit == 0:
    print("0")
if digit < 6 and digit != 0:
    print("less than 6 and not 0")
