# NUM_ELVES = 5
NUM_ELVES = 3014387

class Elf(object):
	def __init__(self,left,id):
		self.left = left
		self.presents = 1
		self.id = id
	def stealLeft(self):
		self.presents += self.left.presents
		self.left = self.left.left

ROOT_ELF = Elf(None,1)
prev_elf = ROOT_ELF
for i in xrange(1,NUM_ELVES):
	new_elf = Elf(prev_elf,i+1)
	prev_elf.left = new_elf
	prev_elf = new_elf
# close circle
prev_elf.left = ROOT_ELF

elf = ROOT_ELF
while True:
	elf.stealLeft()
	if elf == elf.left:
		print "OMG DONE"
		print elf.id,elf.presents
		exit()
		
	elf = elf.left
