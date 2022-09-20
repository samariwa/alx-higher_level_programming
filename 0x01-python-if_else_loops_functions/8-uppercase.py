#!/usr/bin/python3
def uppercase(string):
	result = ''
	for c in range(0, len(string)):
        	if ord(string[c]) >= 97 and ord(string[c]) <= 122:
                	result += "{:s}".format(ord(string[c]))
        	else:
                	result += "{:s}".format(ord(string[c]) - 32)

	print(result)
