#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """ Function the prints out full name based on input names """
    if type(first_name) is  not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
