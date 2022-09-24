#!/usr/bin/env python3


def no_c(my_string):
    new_string = ''

    for c in range(len(my_string)):
        if my_string[c] not in ['c', 'C']:
            new_string += my_string[c]
    

    return(new_string)
