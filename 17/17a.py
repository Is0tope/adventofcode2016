import md5
from Queue import PriorityQueue

# PASSCODE = 'ulqzkmiv'
PASSCODE = 'mmsxrhfx'

MAZE_WIDTH = 4
MAZE_HEIGHT = 4

START_POINT = (0,0)
TARGET_POINT = (3,3)

def manhattanDist(a,b):
	return sum([abs(x-y) for x,y in zip(a,b)])

class Node(object):
	def __init__(self,coords,path,steps=0):
		self.coords = coords
		self.path = path
		self.steps = steps
		self.heuristic = manhattanDist(self.coords,TARGET_POINT)

	def getDoors(self):
		key = md5.new(self.path).hexdigest()[:4]
		return dict(zip('UDLR',[x in 'bcdef' for x in key]))

	def getValidNodes(self):
		doors = self.getDoors()
		nodes = []
		if self.coords[1] < MAZE_HEIGHT -1 and doors['D']:
			nodes.append(Node((self.coords[0],self.coords[1]+1),self.path+'D',self.steps+1))
		if self.coords[1] > 0 and doors['U']:
			nodes.append(Node((self.coords[0],self.coords[1]-1),self.path+'U',self.steps+1))
		if self.coords[0] < MAZE_WIDTH -1 and doors['R']:
			nodes.append(Node((self.coords[0]+1,self.coords[1]),self.path+'R',self.steps+1))
		if self.coords[0] > 0 and doors['L']:
			nodes.append(Node((self.coords[0]-1,self.coords[1]),self.path+'L',self.steps+1))
		return nodes
	def __repr__(self):
		return str(self.steps)+" "+str(self.coords)+" "+str(self.path)+" "+str(self.heuristic)

QUEUE = PriorityQueue()
START_NODE = Node(START_POINT,PASSCODE)

QUEUE.put((0,START_NODE))

MAX_PATH = 0

while QUEUE.qsize()>0:
	item = QUEUE.get()
	node = item[1]
	# print node
	if node.coords == TARGET_POINT:
		# print "OMG DONE"
		# print node.path
		# print node.steps
		# exit(0)
		print "PATH FOUND",node.steps
		if node.steps > MAX_PATH:
			MAX_PATH = node.steps
		continue

	valid_nodes = node.getValidNodes()
	# print "valid nodes: ",len(valid_nodes)
	[QUEUE.put((n.steps,n)) for n in valid_nodes]

print "ALL PATHS EXHAUSTED"
print "MAX_PATH: ",MAX_PATH