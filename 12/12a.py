CODE = []
with open('input.txt') as f:
    CODE = [l.strip().split(' ') for l in f.readlines()]
    
NUM_LINES = len(CODE)
POINTER = 0

#REGISTERS = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
REGISTERS = {'a' : 0, 'b' : 0, 'c' : 1, 'd' : 0}

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
		if val != 0:
			POINTER += int(inst[2])
			continue

	POINTER += 1

print REGISTERS