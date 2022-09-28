#!/usr/bin/python3


def best_score(a_dictionary):
    init = 0
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        if v > init:
            init = v
            best = k
    return(best)
