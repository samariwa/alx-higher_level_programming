#!/usr/bin/python3
""" This module contains an empty class for rectangle """


class Rectangle:
    """ This is the class for rectangle creation """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width = 0, height = 0):
        """ constructor of the rectanlge class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method of class rectangle that takes in 2 Rectangle\
        instances and compare which of them is big. Type checks are done """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ class method for rectangle that returns a new rectangle instance\
        with width and height equal to size """
        return (Rectangle(size, size))

    def area(self):
        """ returns the area of the rectangle """
        return (self.height * self.width)

    def perimeter(self):
        """ returns the perimeter of the rectangle\
        returns 0 if the height of the rectangle is equal to its width """
        if self.height == self.width:
            return 0
        return ((self.height + self.width) * 2)

    def my_rectangle(self):
        """ Prints the area of the rectangle using the # symbol\
        returns an empty string if width or height is 0 """
        area = ''
        if self.width == 0 or self.height == 0:
            return('')
        for w in range(self.width):
            for h in range(self.height):
                area += print_symbol
            area += '\n'
        return (area)

    def __del__(self):
        """ Deconstructor for rectangle instances """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
