#!/usr/bin/python3
""" This module comprises of various classes and methods with some\
inheriting from others """

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the constructor of the base class of this module.\
        It set the value of the id passed in else increments the private\
	variable nb_objects """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

"""
    @property
    def id(self):
        """""" This is the getter method for public atrribute id """"""
        return self.id

    @id.setter
    def id(self, val):
     """   """ This is the setter method for public atrribute id """"""
        self.size = val """
