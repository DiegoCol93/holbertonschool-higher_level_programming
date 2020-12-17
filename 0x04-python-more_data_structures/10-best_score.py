#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        x = (max(sorted(a_dictionary)))
        return x
    else:
        return None
