#!/usr/bin/python3
"""creation of the square class"""  

class Square:
    """constructor of the square class"""
    def __init__(self, size=0):
        """setting size with type and value checkers"""
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    """method that gets are of the square"""
    def area(self):
        """returns the area of the square"""
        return (self.__size ** 2)

    """method that prints the square area using dimensions provided"""
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print('')

    """getter for the size property"""
    @property
    def size(self):
        """returns the size of the square"""
        return (self.__size)

    """setter for the size property"""
    @size.setter
    def size(self, value):
        """setting size with type and value checkers"""
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value
