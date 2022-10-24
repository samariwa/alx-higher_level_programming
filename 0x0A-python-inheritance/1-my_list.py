#!/usr/bin/python3


class list:
    """ This is the super class of this module that contains\
    list comprehension methods"""

    def __init__(self, new_list=[]):
        self.new_list = new_list

    @property
    def new_list(self):
        return self.__new_list

    @new_list.setter
    def new_list(self, new_list):
        self.__new_list = new_list

    def append(self, val):
        self.__new_list.append(val)

    def print_sorted(self):
        sorted_list = self.__new_list[:]
        sorted_list.sort()
        print(sorted_list)

    def __str__(self):
        return "{}".format(self.__new_list)


class MyList(list):
    """ This is the sub-class that inherits from the list class """

    def __init__(self, new_list=[]):
        list.__init__(self, new_list)

    def __str__(self):
        return super().__str__()
