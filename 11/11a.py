# negative is chip, positive generator
# elevator always starts on floor 0
import numpy as np
import operator
import copy
from Queue import Queue
import sys

def isChip(o):
	if o < 0:
		return True

class State(object):
	def __init__(self,arr,step=0,elevator=0):
		self.arr = arr
		self.step = step
		self.elevator = elevator
	def findItem(self,item):
		for i,x in enumerate(self.arr):
			if item in x:
				return i
	def applyChange(self,objs,dir):
		for o in objs:
			idx = self.findItem(o)
			self.arr[idx].remove(o)
			self.arr[idx+dir].add(o)
		self.step += 1
		self.elevator += dir
	def isRowValid(self,row):
		if len(row) < 2:
			return True
		if all([x<0 for x in row]):
			return True
		for o in row:
			if isChip(o):
				if not (-1*o) in row:
					return False
		return True
	def isValid(self):
		for r in self.arr:
			if not self.isRowValid(r):
				return False
		return True
	def compare(self,state):
		return all([x == y for x,y in zip(self.arr,state.arr)]+[self.elevator==state.elevator])
	def getValidStates(self):
		avail_dirs = []
		if self.elevator >= 0 and self.elevator < 3:
			avail_dirs.append(1)
		if self.elevator > 0 and self.elevator <= 3:
			avail_dirs.append(-1)
		ret = []
		# check on levels
		erow = self.arr[self.elevator]
		for o in erow:
			for d in avail_dirs:
				s = copy.deepcopy(self)
				s.applyChange([o],d)
				if s.isValid():
					ret.append(s)
				# combos
				for t in erow:
					if t == o:
						continue
					s = copy.deepcopy(self)
					s.applyChange([o,t],d)
					if s.isValid():
						ret.append(s)
		return ret
	def getRotationStates(self):
		num_pairs = sum(map(len,self.arr)) / 2
		items = range(1,num_pairs+1)
		states = []
		for i in xrange(1,num_pairs):
			fulldict = dict(zip(items,np.roll(items,i)))
			negdict = dict(zip(np.negative(items),np.roll(np.negative(items),i)))
			fulldict.update(negdict)
			s = copy.deepcopy(self)
			s.arr = [set([fulldict[x] for x in floor]) for floor in self.arr]
			states.append(s)
		return states

	def __repr__(self):
		return str([sorted(list(x)) for x in self.arr])+str(self.elevator)
	def __hash__(self):
		return hash(self.__repr__())

# calc init state
INIT_ARR = []
with open('input.txt') as f:
	for l in f:
		l = l.strip().split(' ')
		INIT_ARR.append(set([int(x) for x in l]))
	INIT_ARR.append(set())
INIT_STATE = State(INIT_ARR)

# calc final state
FINAL_ARR = [set() for x in xrange(len(INIT_ARR)-1)]
FINAL_ARR.append(reduce(operator.__or__,INIT_ARR))
FINAL_STATE = State(FINAL_ARR)
FINAL_STATE.elevator = 3

print "INITIAL STATE: ",INIT_STATE
print "FINAL STATE: ",FINAL_STATE

# execution
QUEUE = Queue()
SEEN_STATES = set()

# loop
cnt = 0
QUEUE.put(INIT_STATE)
while QUEUE:
	if QUEUE.qsize() == 0:
		exit(1)
	state = QUEUE.get()
	# print "STATE",state.arr,state.elevator
	# is it final state
	if FINAL_STATE.compare(state):
		print "DONE OMG"
		print state.arr
		print state.elevator
		print state.step
		exit(0)
	# seen before?
	if hash(state) in SEEN_STATES:
		continue
	# branch
	new_states = state.getValidStates()
	if 0 == cnt % 1000:
		print "COUNT: {}, STEP: {}".format(cnt,state.step)
	# if new_states:
		#print "Found {} valid states @ step {}".format(len(new_states),state.step)
	# for s in new_states:
	# 	print s.arr,s.elevator
	[QUEUE.put(s) for s in new_states]
	# add to seen states
	SEEN_STATES.add(hash(state))
	# add all rotations to seen states
	[SEEN_STATES.add(hash(x)) for x in state.getRotationStates()]
	cnt += 1