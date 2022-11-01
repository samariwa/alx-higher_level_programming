#!/usr/bin/python3
""" Unit tests for square.py module """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquareClass(unittest.TestCase):
    """ This is a test class for the various methods of the Square class """
    def test_instantiation_with_valid_args(self):
        """ This tests for instantiation with a valid argument """
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.id, 5)

    def test_instantiation_without_some_arg(self):
        """ This tests for instantiation without any argument\
        The number of instances initialised without an id should\
        be id assigned to that object """
        square = Square(7)
        self.assertEqual(square.size, 7)

    def test_square_is_instance_of_base(self):
        """ This checks if square object is an instance of Base class """
        self.assertIsInstance(Square( 12), Base)

    def test_size_getter(self):
        """ This checks if the getter method for the size attribute is ok """
        square = Square(5)
	self.assertEqual(5, square.size)

    def test_size_setter(self):
        """ This checks if the setter method for the size attribute is ok """
        square = Square(5)
	square.size = 7
        self.assertEqual(7, square.size)

    def test_x_getter(self):
        """ This checks if the getter method for the x attribute is ok """
        square = Square(5, 12, 16, 6)
        self.assertEqual(12, square.x)
               
    def test_x_setter(self):
        """ This checks if the setter method for the x attribute is ok """
        square = Square(5, 12, 16, 6)
        square.x = 15
        self.assertEqual(15, square.x)

    def test_y_getter(self):
        """ This checks if the getter method for the y attribute is ok """
        square = Square(5, 12, 16, 6)
        self.assertEqual(16, square.y)
               
    def test_y_setter(self):
        """ This checks if the setter method for the y attribute is ok """
        square = Square(5, 12, 16, 6)
        square.y = 20
        self.assertEqual(20, square.y)

    def test_zero_size(self):
        """ This test case checks if an exception is raised when 0 is set as\
        the square width """
	with self.assertRaises(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_width(self):
        """ This test case checks if an exception is raised when a negative number\
        is set as the square width """
        with self.assertRaises(ValueError, "width must be > 0"):
            Square(-2)

    def test_type_width(self):
        """ This test case checks if an exception is raised when a non-integer\
        is set as the square width """
        with self.assertRaises(TypeError, "width must be an integer"):
            Square('w')

