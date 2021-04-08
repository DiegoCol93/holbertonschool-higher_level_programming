#!/usr/bin/python3
# module for storing find_peak funtion.


def find_peak(list_of_integers):
    """ Finds the maximum number on a list. """
    if bool(list_of_integers):
        list_of_integers.sort()
        return(list_of_integers[-1])
