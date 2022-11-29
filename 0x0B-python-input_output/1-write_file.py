#!/usr/bin/python3
""" This module contains a function that writes a string to a text file """


def write_file(filename="", text=""):
    """ This function opens the text file passed in and\
    writes the accompanying content in it """
    if filename and text:
        with open(filename, mode='w', encoding='UTF8') as fd:
            return fd.write(text)
