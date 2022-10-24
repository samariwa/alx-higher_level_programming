#!/usr/bin/python3


"""
This module contains the lookup class that returns the attributes of an object
"""
def lookup(obj):
    """ This class returns a list of all attributes\
    (variables and methods) in the object passed as a parameter"""
    return dir(obj)
