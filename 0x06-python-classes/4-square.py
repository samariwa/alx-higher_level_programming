#!/usr/bin/python3
""" creation of the square class """  


class Square:
    """ constructor of the square class """
    def __init__(self, size=0):
        """ initialization of the private attribute size based on 
        input checker
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """ returns the area of the square """
        return (self.__size ** 2)

    @property
    def size(self):
        """ returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
    """ setting size with type and value checkers
    args:
        value: the size parameter in __init__
    """
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value
