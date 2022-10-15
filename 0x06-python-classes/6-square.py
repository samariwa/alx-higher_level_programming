#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a module for a square class with private args that can calculate area

Example:
    This module is expected to have a Class with private args
    The said file imports it as follows:
    Square = __import__('3-square').Square
    The outcome expected looks like this
    $ ./6-main.py | tr " " "_" | cat -e
    ###$
    ###$
    ###$
    --$
    _###$
    _###$
    _###$
    --$
    ___###$
    ___###$
    """


class Square:
    """ creates an a class with a private attribute size """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the instance and enforce the type
        of size to be a positive integer
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
        """ returns the area of the square """
        return (self.__size ** 2)i

    def my_print(self):
        """ prints the square based on the size """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print('')

    @property
    def size(self):
        """ getter of the size property """
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

    @property
    def position(self):
        """ returns the position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ setting size with type and value checkers

        args:
            value: the position parameter in __init__
        """

        for point in value:
            if type(point) is int or point >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple\
                                 of 2 positive integers")
