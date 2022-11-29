#!/usr/bin/python3
""" This is a module that contains a class BaseGeometry """


class BaseGeometry:
    """ This is the BaseGeometry class. It is the super class of the module """
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
