#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_matrix = sorted(a_dictionary.items())

    for line in sorted_matrix:
        print("{}: {}".format(line[0], line[1]))
