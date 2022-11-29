#!/usr/bin/python3
""" This module has a functions that checks if an object is an instance\
of the specified class """


def is_same_class(obj, a_class):
    """ This is a function that returns True if the object is exactly an\
    instance of the specified class; otherwise False """
    return type(obj) == a_class
