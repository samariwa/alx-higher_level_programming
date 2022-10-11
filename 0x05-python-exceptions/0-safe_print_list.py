#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                print(i, end='')
                count += 1
        print('')
        if count < x:
            raise ValueError
    except ValueError:
        pass

    return (count)
