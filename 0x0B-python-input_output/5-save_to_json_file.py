#!/usr/bin/python3
""" This module contains a function that writes to a file a string\
from the object passed in """
import json


def save_to_json_file(my_obj, filename):
    """ This function converts an object to JSON and writes it to file """
    with open(filename, mode='w', encoding='UTF8') as fd:
        fd.write(json.dumps(my_obj))
