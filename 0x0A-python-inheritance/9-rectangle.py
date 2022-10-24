#!/usr/bin/python3
""" This is a module that contains a class BaseGeometry """


class BaseGeometry:
    """ This is the BaseGeometry class. It is the super class of the module """
    def area(self, *args):
        pass

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator(width, width)
        self.__width = width
        super().integer_validator(height, height)
        self.__height = height

    def print(self, value):
        print(value)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
