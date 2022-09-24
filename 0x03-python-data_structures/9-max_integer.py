#!/usr/bin/python3


def max_integer(my_list=[]):
    maxim = 0
    if not my_list:
        return("None")

    for i in range(len(my_list)):
        if my_list[i] > maxim:
            maxim = my_list[i]

    return(maxim)
