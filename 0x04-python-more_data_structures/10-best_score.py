#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        return max(sorted(a_dictionary))
    else:
        return None
