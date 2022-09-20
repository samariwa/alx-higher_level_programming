#!/usr/bin/python3
for s in range(0, 100):
    if s == 99:
        nxt = '\n'
    else:
        nxt = ', '

    print("{:02d}".format(s), end=nxt)
