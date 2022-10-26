#!/usr/bin/python3
""" This module contains a function that converts a JSON string in\
a file to an object """
import json


def load_from_json_file(filename):
    """ This function converts JSON string in a file to an object """
    with open(filename, mode='r', encoding='UTF8') as fd:
        return json.loads(fd.read())
