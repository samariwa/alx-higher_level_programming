#!/usr/bin/python3


def add_result():
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    from add_0 import add
    add_result()
