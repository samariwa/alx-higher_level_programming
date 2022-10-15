#!/usr/bin/python3
"""creation of the square class"""


class Square:
    """constructor of the square class"""
    def __init__(self, size=0):
        """initialization of the private attribute\
        size based on input checker"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
