class Node(object):
	def __init__(self,x,y,size,used,avail):
		self.x = x
		self.y = y
		self.size = size
		self.used = used
		self.avail = avail

NODES = []
with open('input.txt') as f:
    for l in f:
    	data = l.split()
    	x,y = map(int,[x[1:] for x in data[0].split('-')[1:]])
    	size = int(data[1][:-1])
    	used = int(data[2][:-1])
    	avail = int(data[3][:-1])

    	NODES.append(Node(x,y,size,used,avail))

viable_pairs = 0
for i,node1 in enumerate(NODES):
	for j,node2 in enumerate(NODES):
		if j == i:
			continue
		if node1.used == 0:
			continue
		if node1.used <= node2.avail:
			viable_pairs += 1

print "VIABLES PAIRS: ",viable_pairs
