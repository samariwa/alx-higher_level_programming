#!/usr/bin/python3
"""Square class creation"""

class Square:
    """Constructor of the square class"""
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self._size = size

    """gets the area of the square using size provided"""
    def area(self):
	"""returns the area of the square"""
        return (self._size ** 2)

    """prints a square area using the size provided"""
    def my_print(self):
        for i in range(self._size):
            for j in range(self._size):
                print("#", end='')
            print('')

    """getter of the size property"""
    @property
    def size(self):
        return (self._size)

    """setter of the size property"""
    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self._size = value

    """"getter of the position property"""
    @property
    def position(self):
        """returns the position of the square"""
        return (self._position)

    """setter of the position property"""
    @position.setter
    def position(self, value):
        for point in value:
            if type(point) is int or point >= 0:
                self._position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
