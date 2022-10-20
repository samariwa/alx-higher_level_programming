#!/usr/bin/python3


def text_indentation(text):
    """ function that prints a text with 2 new lines after\
    each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    breakers = ['.', '?', ':']
    new_text = ''
    count = 0
    text_list = list(text)

    for character in text_list:
        new_text += character
        if character in breakers:
            text_list[count + 1] += '\n\n'
        count += 1

    print(new_text, end='')
