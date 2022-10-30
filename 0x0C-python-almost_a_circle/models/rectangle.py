#!/usr/bin/python3
""" This module contains a class (Rectangle) which is a subclass of\
Base class and inherits some of its attributes such as 'id'
"""
from models.base import Base


class Rectangle(Base):
    """ This is the subclass of superclass Base and it inherits some\
    of its attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the constructor of the class Rectangle and initialization\
	of some of its attributes is done after checkers of type and value are\
	done """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @property
    def width(self):
        """ This is the getter of the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the setter of the width attribute together with value\
        type checkers """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ This is the getter of the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the setter of the x attribute together with value\
        type checkers """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__width = value

    @property
    def x(self):
        """ This is the getter of the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ This is the setter of the x attribute together with value\
        type checkers """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ This is the getter of the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ This is the setter of the x atrribute together with value\
        type checkers """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This is a public method that returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ This is a public method that prints the rectangle representation\
        using the # symbol in string format """
        for height in range(self.__height):
            for width in range(self.__width):
                print('#', end='')
            print()
