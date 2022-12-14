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
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ This function returns a representation of the\
        string instance in string format """
        return "[Square] ({}) {}/{} - {}\
        ".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ This is the getter of the width attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ This is the setter of the width attribute together with value\
        type checkers """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ This function updates the value of the attributes using the\
        values passed in as arguments in the specific order"""
        if args is not None and len(args) != 0:
            try:
                if args[0] is not None:
                    self.id = args[0]
                if args[1] is not None:
                    self.width = args[1]
                    self.height = args[1]
                if args[2] is not None:
                    self.x = args[2]
                if args[3] is not None:
                    self.y = args[3]
            except IndexError:
                pass
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.width = value
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ This method returns a dictionary containing the various\
        and values of the instance """
        attributes = {'id': self.id,
                      'size': self.width,
                      'x': self.x,
                      'y': self.y}
        return attributes
