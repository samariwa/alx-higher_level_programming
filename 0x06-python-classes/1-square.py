#!/usr/bin/python3
"""a module for a square class with private args
Example:
    This module is expected to have a Class with private args
        $ ./1-main.py
        <class '1-square.Square'>
        {'_Square__size': 3}
        'Square' object has no attribute 'size'
        'Square' object has no attribute '__size'
"""

class Square:
    """a class Square that defines a square
       private instance attribute: size
       Instantiation with size
    """
    def __init__(self, size):
	"""initialization of the square object
           Args:
               _size (int): length of the square which is a private attribute
        """
        self._size = size
