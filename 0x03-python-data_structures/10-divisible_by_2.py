#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if my_list:
        list_TF = []
        index = 0
        for i in my_list:
            if i % 2 == 0:
                list_TF.append(True)
            else:
                list_TF.append(False)
                index += 1
        return list_TF
