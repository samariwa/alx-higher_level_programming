#!/usr/bin/python3
""" This module contains a function that reads an input file and\
prints its content to the standard output """

def read_file(filename=""):
    """ this function opens the provided file and prints its content\
    to stdout """
    with open(filename, mode='r', encoding='UTF8') as fd:
        print(fd.read(), end='')
