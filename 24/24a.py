from Queue import PriorityQueue
from operator import itemgetter
from copy import deepcopy
from collections import OrderedDict

def manhattanDist(a,b):
	return sum([abs(x-y) for x,y in zip(a,b)])

class State(object):
	def __init__(self,maze,coords,objects,step):
		self.maze = maze
		self.coords = coords
		self.objects = objects
		self.step = step
		self.mazesize = sum([len(x) for x in maze])
		# heuristic distance to closest item for now
		if objects:
			# TODO: used sorted dict or something
			# minKey = min(objects.keys())
			# self.H = manhattanDist(coords,objects[minKey]) + step + (self.mazesize * len(objects))
			self.H = step 
		else:
			self.H = 0

	def createState(self,newcoords):
		x,y = newcoords
		objects = deepcopy(self.objects)
		c = self.maze[y][x]
		if not c in ('#','.'):
			# handle exit node
			# is it the last object
			if int(c) in objects:
				if not int(c) == EXIT_OBJECT:
					del objects[int(c)]
				elif len(objects)==1:
					del objects[int(c)]

		return State(self.maze,newcoords,objects,self.step+1)

	def getValidStates(self):
		valid = []
		x,y = self.coords
		if self.maze[y][x-1] != '#':
			valid.append(self.createState((x-1,y)))
		if self.maze[y][x+1] != '#':
			valid.append(self.createState((x+1,y)))
		if self.maze[y-1][x] != '#':
			valid.append(self.createState((x,y-1)))
		if self.maze[y+1][x] != '#':
			valid.append(self.createState((x,y+1)))
		return valid

	def __str__(self):
		return "STATE {} {} S: {} H: {}".format(self.coords,self.objects.keys(),self.step,self.H)

	def __hash__(self):
		return hash("{}{}".format(self.coords,self.objects.keys()))

MAZE = []
OBJECT_LIST = []
START_COORDS = None

with open('input.txt') as f:
	f = f.readlines()
	for y,l in enumerate(f):
		line = []
		for x,c in enumerate(l.strip()):
			if not c in ('#','.'):
				if c == '0':
					START_COORDS = (x,y)
					# c = '.'
				else:
					OBJECT_LIST.append((int(c),(x,y)))
			line.append(c)
		MAZE.append(line)


# sort objects for later
OBJECT_LIST.sort(key=itemgetter(0))
OBJECTS = OrderedDict(OBJECT_LIST)

# extra for part B
# add a final special objective at the same starting coordinates
EXIT_OBJECT = 0
OBJECTS[EXIT_OBJECT] = (START_COORDS)

QUEUE = PriorityQueue()
SEEN_STATES = set()
QUEUED_STATES = set()

# add first state
INITIAL_STATE = State(MAZE,START_COORDS,deepcopy(OBJECTS),0)
QUEUE.put((INITIAL_STATE.H,INITIAL_STATE))
print OBJECTS
print EXIT_OBJECT
while QUEUE.qsize():
	priority,state = QUEUE.get()

	print state

	# victory condition
	if len(state.objects) == 0:
		print "OMG DONE"
		print "STEPS: " + str(state.step)
		exit()

	# next states
	valid = state.getValidStates()
	for v in valid:
		hv = hash(v)
		if hv in SEEN_STATES or hv in QUEUED_STATES:
			continue
		# print"    ",v
		QUEUE.put((v.H,v))
		QUEUED_STATES.add(hash(v))
	
	SEEN_STATES.add(hash(state))
