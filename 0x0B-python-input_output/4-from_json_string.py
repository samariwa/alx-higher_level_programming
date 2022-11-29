#!/usr/bin/python3
""" This module contains a function that returns an object\
from the JSON representation passed in """
import json


def from_json_string(my_str):
    """ This function converts an object to JSON notation and returns it """
    return json.loads(my_str)
