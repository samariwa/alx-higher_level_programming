#!/usr/bin/env python3


def no_c(my_string):
    new_string = ''
    count = 0

    for c in range(len(my_string)):
        if my_string[c] == 'C' or my_string[c] == 'c':
            new_string = my_string[:c] + my_string[c + 1:]
            count += 1
    
    if count == 0:
        new_string = my_string

    return(new_string)
