#!/usr/bin/python3
""" This module contains a function that appends a string to a text file """


def append_write(filename="", text=""):
    """ This function opens the text file passed in and\
    appends the accompanying content in it """
    if filename and text:
        with open(filename, mode='a', encoding='UTF8') as fd:
            return fd.write(text)
