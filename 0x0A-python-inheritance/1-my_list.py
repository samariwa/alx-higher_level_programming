#!/usr/bin/python3
""" This module contains the list class that has various list comprehension\
methods. It also has a child class MyList that inherits its attributes """


class list:
    """ This is the super class of this module that contains\
    list comprehension methods"""

    def __init__(self, new_list=[]):
        """ This is the constructor of the super class list """
        self.new_list = new_list

    @property
    def new_list(self):
        """ this is the getter method of the list attribute """
        return self.__new_list

    @new_list.setter
    def new_list(self, new_list):
        """ This is the setter method for the list attribute """
        self.__new_list = new_list

    def append(self, val):
        """ This is the append method that appends values to the list """
        self.__new_list.append(val)

    def print_sorted(self):
        """ This the method that sorts the list and print it """
        sorted_list = self.__new_list[:]
        sorted_list.sort()
        print(sorted_list)

    def __str__(self):
        """ This method print a stringifyed representation of an instance """
        return "{}".format(self.__new_list)


class MyList(list):
    """ This is the sub-class that inherits from the list class """

    def __init__(self, new_list=[]):
        """ This is the constructor of the sub class mylist """
        list.__init__(self, new_list)

    def __str__(self):
        """ This method that prints the stringifyed represntation the list\
        and it inherits a super class method """
        return super().__str__()
