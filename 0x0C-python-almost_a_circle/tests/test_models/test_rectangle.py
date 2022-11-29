#!/usr/bin/python3
""" Unit tests for rectangle.py module """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestRectangleClass(unittest.TestCase):
    """ This is a test class for the various methods of the Rectangle class """
    def test_instantiation_with_valid_args(self):
        """ This tests for instantiation with a valid argument """
        rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle.id, 5)

    def test_instantiation_without_some_arg(self):
        """ This tests for instantiation without any argument\
        The number of instances initialised without an id should\
        be id assigned to that object """
        rectangle = Rectangle(2, 7)
        self.assertEqual(rectangle.width, 2)

    def test_rectangle_is_instance_of_base(self):
        """ This checks if rectangle object is an instance of Base class """
        self.assertIsInstance(Rectangle(23, 12), Base)

    def test_width_getter(self):
        """ This checks if the getter method for the width attribute is ok """
        rectangle = Rectangle(5, 10)
        self.assertEqual(5, rectangle.width)

    def test_width_setter(self):
        """ This checks if the setter method for the width attribute is ok """
        rectangle = Rectangle(5, 10)
        rectangle.width = 7
        self.assertEqual(7, rectangle.width)

    def test_height_getter(self):
        """ This checks if the getter method for the height attribute is ok """
        rectangle = Rectangle(5, 10)
        self.assertEqual(10, rectangle.height)
               
    def test_height_setter(self):
        """ This checks if the setter method for the height attribute is ok """
        rectangle = Rectangle(5, 10)
        rectangle.height = 12
        self.assertEqual(12, rectangle.height)

    def test_x_getter(self):
        """ This checks if the getter method for the x attribute is ok """
        rectangle = Rectangle(5, 10, 12, 16, 6)
        self.assertEqual(12, rectangle.x)
               
    def test_x_setter(self):
        """ This checks if the setter method for the x attribute is ok """
        rectangle = Rectangle(5, 10, 12, 16, 6)
        rectangle.x = 15
        self.assertEqual(15, rectangle.x)

    def test_y_getter(self):
        """ This checks if the getter method for the y attribute is ok """
        rectangle = Rectangle(5, 10, 12, 16, 6)
        self.assertEqual(16, rectangle.y)
               
    def test_y_setter(self):
        """ This checks if the setter method for the y attribute is ok """
        rectangle = Rectangle(5, 10, 12, 16, 6)
        rectangle.y = 20
        self.assertEqual(20, rectangle.y)

    def test_zero_width(self):
        """ This test case checks if an exception is raised when 0 is set as\
        the rectangle width """
        with self.assertRaises(ValueError, "width must be > 0"):
            Rectangle(0, 45)

    def test_negative_width(self):
        """ This test case checks if an exception is raised when a negative number\
        is set as the rectangle width """
        with self.assertRaises(ValueError, "width must be > 0"):
            Rectangle(-2, 45)

    def test_type_width(self):
        """ This test case checks if an exception is raised when a non-integer\
        is set as the rectangle width """
        with self.assertRaises(TypeError, "width must be an integer"):
            Rectangle('w', 45)

    def test_zero_height(self):
        """ This test case checks if an exception is raised when 0 is set as\
        the rectangle height """
        with self.assertRaises(ValueError, "height must be > 0"):
            Rectangle(12, 0)

    def test_negative_height(self):
        """ This test case checks if an exception is raised when a negative number\
        is set as the rectangle height """
        with self.assertRaises(ValueError, "height must be > 0"):
            Rectangle(12, -23)

    def test_type_height(self):
        """ This test case checks if an exception is raised when a non-integer\
        is set as the rectangle height """
        with self.assertRaises(TypeError, "height must be an integer"):
            Rectangle(36, 'h')
