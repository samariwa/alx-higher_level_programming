#!/usr/bin/python3
""" This module comprises of various classes and methods with some\
inheriting from others """
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the constructor of the base class of this module.\
        It set the value of the id passed in else increments the private\
	variable nb_objects """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This is a static method that returns the JSON string\
        representation of list_dictionaries """
        if list_dictionaries == None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method writes a JSON string representation to a file """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='UTF-8') as fd:
            if list_objs == None:
                fd.write('[]')
            str_content = []
            for i in list_objs:
                str_content += Base.to_json_string(i.to_dictionary())
            fd.write(json.dumps(str_content))
