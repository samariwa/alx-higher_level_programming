#!/usr/bin/python3


def text_indentation(text):
    """ function that prints a text with 2 new lines after\
    each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    breakers = ['.', '?', ':']
    new_text = ''

    for character in text:
        new_text += character
        if character in breakers:
            new_text += '\n\n'

    print(new_text, end='')
