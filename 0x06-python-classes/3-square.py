#!/usr/bin/python3
"""creation of the square class"""  

class Square:
   """constructor of the square class"""
    def __init__(self, size=0):
        """initialization of the private attribute size based on input checker"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    """method that gets the area of the given square"""
    def area(self):
        """returns the area of the square"""
        return (self.__size * self._size)
