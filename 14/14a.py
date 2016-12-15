import md5
import re
from operator import itemgetter

# salt = "abc"
salt = "ngcjuoqr"

# regex
match3 = re.compile(r'(.)\1{2}')
match5 = re.compile(r'(.)\1{4}')

class HashManager(object):
	def __init__(self):
		self.hashes = {}
	def insert(self,char,hsh):
		if not char in self.hashes:
			self.hashes[char] = []
		self.hashes[char].append(hsh)
	def sweepHashes(self,keys,cnt):
		sweep = []
		for k in self.hashes.keys():
			hshs = self.hashes[k]
			if len(hshs)==0:
				continue
			# if matched, add to list and remove
			if hshs[0][1] == cnt:
				if hshs[0][3]:
					sweep.append(hshs[0])
				self.hashes[k].pop(0)
		if sweep:
			keys += sorted(sweep,key=itemgetter(0))

def stretchedHash(val,n):
	hsh = md5.new(val).hexdigest()
	for x in xrange(n):
		hsh = md5.new(hsh).hexdigest()
	return hsh


KEYS = []
HASHES = HashManager()

cnt = 0

while len(KEYS)<64:
	hsh = stretchedHash(salt+str(cnt),2016)

	five = match5.findall(hsh)
	if len(five):
		for c in five:
			if not c in HASHES.hashes:
				continue
			hashes = HASHES.hashes[c]
			for index,val in enumerate(hashes):
				i,lim,h,matched = val
				if cnt<=lim:
					# update matched state to true
					HASHES.hashes[c][index][3] = True
					print "KEY",i,h
			# HASHES.hashes[c] = []
	three = match3.findall(hsh)
	if len(three)>0:
		HASHES.insert(three[0],[cnt,cnt+1000,hsh,False])
	# sweep hashes
	HASHES.sweepHashes(KEYS,cnt)
	cnt+=1

print "DONE"
for i,k in enumerate(KEYS):
	print i,k[0],k[2]