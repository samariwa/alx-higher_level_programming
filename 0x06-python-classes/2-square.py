#!/usr/bin/python3
"""creation of the square class"""

class Square:
    """constructor of the square class"""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self._size = size
