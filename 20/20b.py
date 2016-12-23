BLACKLIST = []
from operator import itemgetter

with open('input.txt') as f:
    for l in f:
    	l,u = [int(x) for x in l.strip().split('-')]
    	BLACKLIST.append((l,u))

BLACKLIST.sort(key=itemgetter(0))
VALID_IPS = []
MAX_IP = 4294967295
current_lowest = 0
last_black = 0
for i in xrange(len(BLACKLIST)):
	l,u = BLACKLIST[i]
	if current_lowest < l:
		VALID_IPS.extend(range(current_lowest,l))
		current_lowest = l-1
	if current_lowest < u:
		current_lowest = u+1
	if last_black < u:
		last_black = u

if last_black < MAX_IP:
	VALID_IPS.extend(range(last_black+1,MAX_IP+1))

print VALID_IPS
print len(VALID_IPS)