#!/usr/bin/python3
"""This module entails creation of the square class
   and initialization of the size priperty in the class
   constructor

   Example: This module will have a class with private args
   $ ./1-main.py
   <class '1-square.Square'>
   {'_Square__size': 3}
   'Square' object has no attribute 'size'
   'Square' object has no attribute '__size'
"""

class Square:
    """constructor of the square class"""
    def __init__(self, size):
	"""initialization of the private attribute size"""
        self._size = size
