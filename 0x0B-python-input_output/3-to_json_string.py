#!/usr/bin/python3
""" This module contains a function that returns a JSON representation\
of the object passed in """
import json


def to_json_string(my_obj):
    """ This function converts an object to JSON notation and returns it """
    return json.dumps(my_obj)
