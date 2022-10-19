#!/usr/bin/python3


def add_integer(a, b=98):
    """ function that adds 2 integers\
    checkers for value input are also set"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
