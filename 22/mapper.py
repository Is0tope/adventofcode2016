import numpy as np
import copy
from Queue import PriorityQueue
import sys
class Node(object):
	def __init__(self,x,y,size,used,avail):
		self.x = x
		self.y = y
		self.size = size
		self.used = used
		self.avail = avail
	def __str__(self):
		return str(self.used) + "/" + str(self.size)

	def __repr__(self):
		return str(self)

NODES = []
with open('input.txt') as f:
    for l in f:
    	data = l.split()
    	x,y = map(int,[x[1:] for x in data[0].split('-')[1:]])
    	size = int(data[1][:-1])
    	used = int(data[2][:-1])
    	avail = int(data[3][:-1])

    	NODES.append(Node(x,y,size,used,avail))

LX = max([x.x for x in NODES])
LY = max([x.y for x in NODES])
DATA_COORDS = (LX,0)
TARGET = (0,0)

GRID = [[0 for x in range(LX+1)] for y in range(LY+1)] 
for i,node in enumerate(NODES):
	if node.used == 0:
		EMPTY_COORDS = (node.x,node.y)
	if (node.x,node.y) == DATA_COORDS:
		node.isData = True
	GRID[node.y][node.x] = node



MAX_AVAIL = max([x.avail for x in NODES])
print MAX_AVAIL

for i in xrange(LX+1):
	for j in xrange(LY+1):
		node = GRID[j][i]
		if (i,j) == DATA_COORDS:
			sys.stdout.write('D')
			continue
		if (i,j) == EMPTY_COORDS:
			sys.stdout.write('_')
			continue
		if (i,j) == TARGET:
			sys.stdout.write('0')
			continue
		if node.used > MAX_AVAIL:
			sys.stdout.write('#')
		else:
			sys.stdout.write('.')

	sys.stdout.write('\n')