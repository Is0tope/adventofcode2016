# INPUT = '10000'
INPUT = '10001110011110000'

# DISK_SIZE = 20
# DISK_SIZE = 272
DISK_SIZE = 35651584

def factoriseDisk(ds):
	tmp = ds
	fact = 1
	while tmp % 2 == 0:
		tmp /= 2
		fact *= 2
	return fact

# def nextBoundry(C):
# 	yield C
# 	n = 1
# 	while True:
# 		yield (C*(2 ** n)) + (2*n) - 1
# 		n += 1

def boundryGen():
	out = '0'
	cnt = 0
	while True:
		# expand
		if cnt == len(out):
			out += '0' + invert(out)
		yield out[cnt]
		cnt+=1

def invert(s):
	d = {'1':'0','0':'1'}
	return "".join([d[x] for x in reversed(s)])

def checksum(s):
	if len(s) == 1:
		return s
	if checksum(s[:len(s)/2]) == checksum(s[len(s)/2:]):
		return '1'
	else:
		return '0'


def dragonCurve(inpt):
	cnt = 0
	C = len(inpt)
	rev_inpt = invert(inpt)
	bgen = boundryGen()
	while True:
		# is it short
		if cnt<C:
			yield inpt[cnt]
			cnt += 1
			continue
		# is it on a boundry
		if (cnt+1) % (C+1) == 0:
			yield next(bgen)
			cnt += 1
			continue

		pos = ((cnt+1) / (C+1))
		offset = ((cnt+1) % (C+1)) - 1
		if pos % 2 == 0:
			yield inpt[offset]
		else:
			yield rev_inpt[offset]
		cnt += 1


CHECKSUM_FACTOR = factoriseDisk(DISK_SIZE)
CHECKSUM_LENGTH = DISK_SIZE / CHECKSUM_FACTOR
CHECKSUM = ''

gen = dragonCurve(INPUT)

while len(CHECKSUM) < CHECKSUM_LENGTH:
	chunk = [next(gen) for x in xrange(CHECKSUM_FACTOR)]
	# print chunk
	CHECKSUM += checksum(chunk)

print "CHECKSUM: ",CHECKSUM