#!/usr/bin/python3
""" creation of the class Square """


class Square:
    """ constructor of the class with a private attribute size """
    def __init__(self, size=0):
        """ initialization of the private attribute size based on
        input checker
        """
        self.size = size

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
