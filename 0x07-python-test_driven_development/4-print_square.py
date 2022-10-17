#!/usr/bin/python3

def print_square(size):
    """ Function that prints the square with the # character\
    based on the size passed as a parameter """
    for width in range(size):
        for length in range(size):
            print('#', end = '')
        print()
