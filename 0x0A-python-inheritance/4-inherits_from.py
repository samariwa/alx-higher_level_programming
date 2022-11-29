#!/usr/bin/python3
""" This module contains a function that checks if a class is a subclass of§
the specified superclass """


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class\
    that inherited (directly or indirectly) from the specified class;\
    otherwise False """
    if isinstance(obj, a_class):
        return not issubclass(a_class, type(obj))
