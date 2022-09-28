#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_set = set()

    for val_1 in set_1:
        for val_2 in set_2:
            if val_1 not in set_2:
                new_set.add(val_1)
            elif val_2 not in set_1:
                new_set.add(val_2)

    return(new_set)
