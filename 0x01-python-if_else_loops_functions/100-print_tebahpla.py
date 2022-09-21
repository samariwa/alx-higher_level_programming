#!/usr/bin/python3
for s in range(122, 96, -1):
    if s % 2 == 0:
        result = s
    else:
        result = s - 32

    print("{:c}".format(result), end='')
