#!/usr/bin/python3


def print_square(size):
    """ Function that prints the square with the # character\
    based on the size passed as a parameter """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float:
        raise TypeError("size must be an integer")
    for width in range(size):
        for length in range(size):
            print('#', end='')
        print()
