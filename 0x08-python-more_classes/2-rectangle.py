#!/usr/bin/python3
""" This module contains an empty class for rectangle """


class Rectangle:
    """ This is the class for rectangle creation """
    def __init__(self, width=0, height=0):
        """ constructor of the rectanlge class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns the width of the rectangle """
        return self._width

    @width.setter
    def width(self, value):
        """setter method for the width of the rectangle with value checkers"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ returns the height of the rectangle """
        return self._height

    @height.setter
    def height(self, value):
        """setter method for the height of the rectangle with value checkers"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._height = value

    def area(self):
        """ returns the area of the rectangle """
        return (self.height * self.width)

    def perimeter(self):
        """ returns the perimeter of the rectangle\
        returns 0 if the height of the rectangle is equal to its width """
        if self.height == self.width:
            return 0
        return ((self.height + self.width) * 2)
