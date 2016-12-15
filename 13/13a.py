import numpy as np
import sys
from Queue import PriorityQueue

# FAV_NUMBER = 10
FAV_NUMBER = 1350
START = (1,1)
# TARGET = (7,4)
TARGET = (31,39)

class Node(object):
	def __init__(self,coords,G,H,parent):
		self.coords = coords
		self.G = G
		self.H = H
		self.F = G+H
		self.parent = parent
	def __repr__(self):
		return "NODE G={}, H={}, F={} @ ".format(self.G,self.H,self.F) + str(self.coords)

def distance(s,d):
	return sum([abs(x-y) for x,y in zip(s,d)])

def createMaze(n,magic):
	arr = np.zeros((n,n))
	for y,row in enumerate(arr):
		for x,elem in enumerate(row):
			val = (x*x) + (3*x) + (2*x*y) + y + (y*y)
			val += magic
			num_bits = sum(['1'==e for e in bin(val)[2:]])
			if (num_bits % 2) == 0:
				arr[y,x] = 0.0
			else:
				arr[y,x] = 1.0
	return arr

def printMaze(maze,char='#',echar='.',target=None,start=(1,1),path = []):
	for y,row in enumerate(maze):
		for x,elem in enumerate(row):
			if target==(x,y):
				sys.stdout.write('X')
				continue
			if start==(x,y):
				sys.stdout.write('O')
				continue
			if (x,y) in path:
				sys.stdout.write('O')
				continue
			if elem == 1:
				sys.stdout.write(char)
			else:
				sys.stdout.write(echar)

		sys.stdout.write('\n')
	sys.stdout.write('\n')

def getNeighbours(maze,coords):
	x,y = coords
	ret = []
	ret.append((max(0,x-1),y))
	ret.append((min(len(maze)-1,x+1),y))
	ret.append((x,max(0,y-1)))
	ret.append((x,min(len(maze)-1,y+1)))
	return [x for x in ret if not x == coords]

def getPath(node):
	path = []
	while node != None:
		path.append(node.coords)
		node = node.parent
	return path

MAZE = createMaze(40,FAV_NUMBER)

print getNeighbours(MAZE,(40,40))
print distance((10,5),(1,1))

QUEUE = PriorityQueue()
OPEN = {}
CLOSED = {}

INIT_NODE = Node(START,0,0,None)
QUEUE.put((0,INIT_NODE))

while QUEUE.qsize()>0:
	F,node = QUEUE.get()
	print node
	# target reached for part a
	# if node.coords == TARGET:
	# 	print "OMG DONE"
	# 	print node
	# 	print getPath(node)
	# 	printMaze(MAZE,target = TARGET,path=getPath(node))
	# 	exit()

	CLOSED[node.coords] = node

	# part b target, stop if 50 steps reached
	if node.G == 50:
		continue

	#if we hit an edge, expand the maze
	lx,ly = node.coords
	if lx == len(MAZE)-1 or ly == len(MAZE)-1:
		MAZE = createMaze(len(MAZE)+5,FAV_NUMBER)

	for c in getNeighbours(MAZE,node.coords):
		if c in CLOSED:
			continue
		# is it a wall
		if MAZE[c[1],c[0]] == 1:
			continue
		n = Node(c,node.G+1,distance(c,TARGET),node)
		# if in open list need to check parents
		if c in OPEN:
			 if n.G < OPEN[c].G:
			 	OPEN[c] = n
		else:
			OPEN[c] = n
			QUEUE.put((n.F,n))
	# print""
	# printMaze(MAZE,target = TARGET,path=getPath(node))

print len(CLOSED)