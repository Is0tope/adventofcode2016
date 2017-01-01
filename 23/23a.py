CODE = []
with open('input_modified.txt') as f:
    CODE = [l.strip().split(' ') for l in f.readlines()]
    
NUM_LINES = len(CODE)
POINTER = 0

#REGISTERS = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
REGISTERS = {'a' : 12, 'b' : 0, 'c' : 0, 'd' : 0}

def getVal(ins):
	val = None
	# is it a register
	if ins in REGISTERS:
		val = REGISTERS[ins]
	else:
		val = int(ins)
	return val
	
while POINTER < NUM_LINES:
	inst = CODE[POINTER]
	print inst
	print REGISTERS
	if inst[0] == 'cpy':
		val = getVal(inst[1])
		REGISTERS[inst[2]] = val

	if inst[0] == 'inc':
		REGISTERS[inst[1]] += 1

	if inst[0] == 'dec':
		REGISTERS[inst[1]] -= 1

	if inst[0] == 'jnz':
		val = getVal(inst[1])
		dist = getVal(inst[2])
		if val != 0:
			POINTER += dist
			continue

	if inst[0] == 'mlt':
		dest = inst[1]
		a,b = getVal(inst[2]),getVal(inst[3])
		print dest,a,b
		REGISTERS[dest] += a * b
		REGISTERS[inst[2]] = 0
		REGISTERS[inst[3]] = 0

	if inst[0] == 'nop':
		pass

	if inst[0] == 'tgl':
		dist = REGISTERS[inst[1]]
		try:
			target_inst = CODE[POINTER+dist][0]
			if target_inst == 'inc':
				CODE[POINTER+dist][0] = 'dec'
			if target_inst in ('dec','tgl'):
				CODE[POINTER+dist][0] = 'inc'
			if target_inst == 'jnz':
				CODE[POINTER+dist][0] = 'cpy'
			if target_inst == 'cpy':
				CODE[POINTER+dist][0] = 'jnz'
		except:
			print "EXCEPTION"

	POINTER += 1

print REGISTERS