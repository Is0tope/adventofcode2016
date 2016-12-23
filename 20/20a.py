BLACKLIST = []
from operator import itemgetter

with open('input.txt') as f:
    for l in f:
    	l,u = [int(x) for x in l.strip().split('-')]
    	BLACKLIST.append((l,u))

BLACKLIST.sort(key=itemgetter(0))

current_lowest = 0
for i in xrange(len(BLACKLIST)):
	l,u = BLACKLIST[i]
	if current_lowest < l:
		print "OMG DONE"
		print "LOWEST IP: ",current_lowest
		exit()
	if current_lowest < u:
		current_lowest = u+1
