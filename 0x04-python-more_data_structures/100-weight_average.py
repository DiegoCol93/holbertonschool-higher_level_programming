#!/usr/bin/python3
def weight_average(my_list=[]):
    weight = 0.0
    values = 0.0
    for i in my_list:
        values += i[0] * i[1]
        weight += i[1]
    return (values / weight)
