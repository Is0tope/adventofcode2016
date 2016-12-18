import numpy as np
import sys

def nextLine(row):
	ret = []
	for i in xrange(len(row)):
		if i == 0:
			l = False
		else:
			l = row[i-1]
		if i == len(row)-1:
			r = False
		else:
			r = row[i+1]
		c = row[i]
		if (l and c and not r) or (r and c and not l) or (l and not c and not r) or (r and not c and not l):
			ret.append(True)
		else:
			ret.append(False)
	return ret

def printTraps(rows):
	for r in rows:
		for e in r:
			sys.stdout.write('^' if e else '.')
		sys.stdout.write('\n')
	sys.stdout.write('\n')

OUTPUT = []
NUM_ROWS = 40
NUM_ROWS = 400000

with open('input.txt') as f:
    line = [x == '^' for x in f.readline().strip()]
    OUTPUT.append(line)
    prev_line = line
    for i in xrange(NUM_ROWS-1):
    	new_line = nextLine(prev_line)
    	OUTPUT.append(new_line)
    	prev_line = new_line

# this will lag on higher outputs but at this scale doesnt really matter
printTraps(OUTPUT)
print np.sum(np.negative(OUTPUT))
