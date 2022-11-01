#!/usr/bin/python3
""" This module comprises of various classes and methods with some\
inheriting from others """
import json
import os


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
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ This is a static method that returns a list from a\
        JSON string representation """
        if json_string is None:
            return([])
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method writes a JSON string representation to a file """
        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='UTF-8') as fd:
            if list_objs is None:
                fd.write('[]')
            str_content = []
            for i in list_objs:
                str_content.append(i.to_dictionary())
            json_str = Base.to_json_string(str_content)
            fd.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ This method returns an instance with all the attributes already\
        set """
        if cls.__name__ == 'Rectangle':
            instance = cls(1, 1, 1, 1)
        elif cls.__name__ == 'Square':
            instance = cls(1, 1, 1)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ This is a class method that returns the list of instances that\
        were created and saved in the json file """
        filename = cls.__name__ + '.json'
        if os.path.isfile(filename) is False:
            return []
        instances = []
        with open(filename, mode='r', encoding='UTF-8') as fd:
            instance_list = Base.from_json_string(fd.read())
        for instance in instance_list:
            instances.append(cls.create(**instance))

        return instances
