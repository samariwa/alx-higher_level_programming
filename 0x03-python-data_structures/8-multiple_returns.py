#!/usr/bin/python3


def multiple_returns(sentence):
    count = 0

    for i in range(len(sentence)):
        count += 1
    result = ()
    if count == 0:
        letter = 'None'
    else:
        letter = sentence[0]
    result = (count, letter,)

    return(result)
