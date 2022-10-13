#!/usr/bin/python3
  

class Square:
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self._size = size

    def area(self):
        return (self._size ** 2)

    def my_print(self):
        for i in range(self._size):
            for j in range(self._size):
                print("#", end='')
            print('')

    @property
    def size(self):
        return (self._size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self._size = value
