#!/usr/bin/python3

def text_indentation(text):
    breakers = ['.', '?', ':']
    new_text = ''

    for character in text:
        new_text += character
        if character in breakers:
            new_text += '\n\n'

    print(new_text, end = '')
