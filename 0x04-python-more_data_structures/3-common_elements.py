#!/usr/bin/python3


def common_elements(set_1, set_2):
    common_set = set()

    for val_1 in set_1:
        for val_2 in set_2:
            if val_1 == val_2:
                common_set.add(val_2)

    return(common_set)
