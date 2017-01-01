import numpy as np
import copy
from Queue import PriorityQueue


TARGET = (0,0)
EMPTY_COORDS = None

def manhattanDist(a,b):
	return sum([abs(x-y) for x,y in zip(a,b)])

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

class State(object):
	def __init__(self,grid,step,ecoords,dcoords=None):
		self.grid = copy.deepcopy(grid)
		self.dcoords = dcoords
		self.ecoords = ecoords
		self.step = step
		# heuristic is distance between data & target, and empty cell and data
		# self.H = manhattanDist(dcoords,TARGET) + manhattanDist(ecoords,dcoords) + (5*step)
		self.H = step

	def swap(self,n1,n2):
		n1.used,n2.used = n2.used,n1.used

	# empty first
	def swapcoords(self,c1,c2):
		n1 = self.grid[c1[1]][c1[0]]
		n2 = self.grid[c2[1]][c2[0]]
		if self.dcoords == c2:
			self.dcoords = c1
		self.ecoords = c2
		self.swap(n1,n2)

	def getValidStates(self):
		x,y = self.ecoords
		empty = self.grid[y][x]
		valid = []
		# left
		if x > 0 and self.grid[y][x-1].used <= empty.size:
			state = State(copy.deepcopy(self.grid),self.step+1,self.ecoords,self.dcoords)
			state.swapcoords((x,y),(x-1,y))
			valid.append(state)
		# right
		if x < LX and self.grid[y][x+1].used <= empty.size:
			state = State(copy.deepcopy(self.grid),self.step+1,self.ecoords,self.dcoords)
			state.swapcoords((x,y),(x+1,y))
			valid.append(state)
		# up
		if y > 0 and self.grid[y-1][x].used <= empty.size:
			state = State(copy.deepcopy(self.grid),self.step+1,self.ecoords,self.dcoords)
			state.swapcoords((x,y),(x,y-1))
			valid.append(state)
		# down
		if y < LY and self.grid[y+1][x].used <= empty.size:
			state = State(copy.deepcopy(self.grid),self.step+1,self.ecoords,self.dcoords)
			state.swapcoords((x,y),(x,y+1))
			valid.append(state)
		return valid

	def __str__(self):
		return "STATE " + str(self.grid) + str(self.dcoords) + str(self.ecoords)

	def __hash__(self):
		return hash(str(self))

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

# GRID = list([list(x) for x in np.zeros((LX,LY))])
GRID = [[0 for x in range(LX+1)] for y in range(LY+1)] 
for i,node in enumerate(NODES):
	print node.x,node.y
	if node.used == 0:
		EMPTY_COORDS = (node.x,node.y)
	if (node.x,node.y) == DATA_COORDS:
		node.isData = True
	GRID[node.y][node.x] = node

SEEN_STATES = set()

print GRID
print EMPTY_COORDS
print DATA_COORDS

QUEUE = PriorityQueue()
INITIAL_STATE = State(GRID,0,EMPTY_COORDS,DATA_COORDS)

QUEUE.put((INITIAL_STATE.H,INITIAL_STATE))
while QUEUE.qsize() > 0:
	priority,state = QUEUE.get()
	print state,state.step,state.H

	# victory condition
	if state.dcoords == TARGET:
		print "OMG DONE"
		print state
		print state.step
		exit()

	valid = state.getValidStates()
	for v in valid:
		# print "    ",v,v.H
		if not hash(v) in SEEN_STATES:
			QUEUE.put((v.H,v))
	SEEN_STATES.add(hash(state))



