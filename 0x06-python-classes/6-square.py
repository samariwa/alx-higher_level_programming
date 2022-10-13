#!/usr/bin/python3
""" Square class creation """

class Square:
    """ Constructor of the square class """
    def __init__(self, size=0, position=(0, 0)):
        """ setting size and position with type and value checkers """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

    def area(self):
	""" returns the area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ prints the square based on the size """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print('')

    @property
    def size(self):
        """ getter of the size property """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setting size with type and value checkers """
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @property
    def position(self):
        """ returns the position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ setting size with type and value checkers """
        for point in value:
            if type(point) is int or point >= 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
