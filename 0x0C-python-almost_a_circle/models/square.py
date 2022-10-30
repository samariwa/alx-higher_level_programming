#!/usr/bin/python3
""" This module contains a class (Square) which is a subclass of\
a subclass (Rectangle) class and inherits some of its attributes and methods
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the subclass of subclass Rectangle and it inherits some\
    of its attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """ This is the constructor of the class Square and initialization\
        of some of its attributes is done """
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """ This function returns a representation of the string instance in string format """
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.__width, self.__height, self.__x, self.__y)    
