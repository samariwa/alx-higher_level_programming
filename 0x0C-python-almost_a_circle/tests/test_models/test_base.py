#!/usr/bin/python3
""" Unit tests for base.py module """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestBaseClass(unittest.TestCase):
    """ This is a test class for the various methods of the Base class """
    def test_instantiation_with_valid_args(self):
        """ This tests for instantiation with a valid argument """
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_instantiation_without_arg(self):
        """ This tests for instantiation without any argument\
        The number of instances initialised without an id should\
        be id assigned to that object """
        base1 = Base()
        base2 = Base(13)
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 13)
        self.assertEqual(base3.id, 2)

    def test_with_excess_arguments(self):
        """ This test method checks if an exception is raised when excess\
        arguments are passed in the instantiation of a Base object """
        with self.asserRaises(Exception):
            base = Base(2, 45)

    def test__obj_to_json_string(self):
        """ This test case checks if a json encoded string of a list of\
        dictionaries is returned from an object passed as a parameter to\
	the static method to_json_string """
        rectangle = Rectangle(34, 64, 23,5, 5)
        dictionary = rectangle.to_dictionary()
        json_val = Base.to_json_string(dictionary)
        json_string = '{"x": 2, "width": 34, "id": 5, "height": 64, "y": 5}'
        self.assertEqual(sorted(json_val), sorted(json_string))

    def test_obj_from_json_string(self):
        """ This test case checks if an attributes list can be recreated\
	from attributes of the instance stored in a json file """
        instances = [
            {'id': 5, 'width': 13, 'height': 45, 'x': 2, 'y': 4},
            {'id': 7, 'width': 4, 'height': 12, 'x': 3, 'y': 6}
        ]
        json_list = Rectangle.to_json_string(instances)
        list_output = Rectangle.from_json_string(json_list)
        self.assertEqual(list_output, instances)
