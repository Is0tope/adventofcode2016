from Queue import deque

# NUM_ELVES = 5
NUM_ELVES = 3014387

LQUEUE = deque()
RQUEUE = deque()

# populate queues
ELVES = range(1,NUM_ELVES+1)
RQUEUE.extend(ELVES[:1+len(ELVES)/2])
LQUEUE.extendleft(ELVES[1+len(ELVES)/2:])

while True:
	# print "R",RQUEUE
	# print "L",LQUEUE
	tot = len(RQUEUE)+len(LQUEUE)
	if tot % 10000 == 0:
		print tot
	
	# remove elf
	if len(RQUEUE)>len(LQUEUE):
		RQUEUE.pop()
	else:
		LQUEUE.pop()

	# do we only have one left?
	if len(RQUEUE)==1 and len(LQUEUE)==0:
		print "OMG DONE"
		print "FINAL ELF: ",RQUEUE.pop()
		exit()

	# rotate the lists
	LQUEUE.appendleft(RQUEUE.popleft())
	RQUEUE.append(LQUEUE.pop())