#!/usr/bin/python3
i = 0
for s in range(0, 9):
	for t in range(i, 10):
		if s == t:
			pass
		else:
        		if s == 8 and t == 9:
                		nxt = '\n'
        		else:
                		nxt = ', '
		
       			print("{}{}".format(s, t), end=nxt)

	i += 1		
