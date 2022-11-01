#!/usr/bin/python3
""" This module contains a class (Rectangle) which is a subclass of\
Base class and inherits some of its attributes such as 'id'
"""
from models.base import Base


class Rectangle(Base):
    """ This is the Rectangle subclass of superclass Base and it inherits\
    some of its attributes"""
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
        # private instance attributes initialized
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
        """ This is the setter of the height attribute together with value\
        type checkers """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

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
        """ This is the setter of the y atrribute together with value\
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
        for wai in range(self.__y):
            print()
        spaces = ''.join(' ' for ex in range(self.__x))
        for height in range(self.__height):
            print("{}".format(spaces), end='')
            for width in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """ This method updates the value of the attributes using the\
        values passed in as arguments in the specific order"""
        if args is not None and len(args) != 0:
            try:
                if args[0] is not None:
                    self.id = args[0]
                if args[1] is not None:
                    self.__width = args[1]
                if args[2] is not None:
                    self.__height = args[2]
                if args[3] is not None:
                    self.__x = args[3]
                if args[4] is not None:
                    self.__y = args[4]
            except IndexError:
                pass
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self._height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ This method returns a dictionary containing the various\
        and values of the instance """
        attributes = {'id': self.id,
                      'width': self.__width,
                      'height': self.__height,
                      'x': self.__x,
                      'y': self.__y}
        return attributes

    def __str__(self):
        """ This function returns a representation of the rectangle\
        instance in string format """
        return "[Rectangle] ({}) {}/{} - {}/{}\
        ".format(self.id, self.__x, self.__y, self.__width, self.__height)
