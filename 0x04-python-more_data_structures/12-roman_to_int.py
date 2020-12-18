#!/usr/bin/python3
def roman_to_int(roman_string):

    let_dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    i = 0
    if isinstance(roman_string, str) and roman_string is not None:
        while i < len(roman_string):
            if (i < (len(roman_string) - 1) and
                    let_dic[roman_string[i + 1]] > let_dic[roman_string[i]]):
                res -= let_dic[roman_string[i]]
            else:
                res += let_dic[roman_string[i]]
            i += 1
    return res
