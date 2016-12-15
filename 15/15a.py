import numpy as np

# settings
# wheels = np.array([5,2])
# offsets = np.array([4,1])
wheels = np.array([13,17,19,7,5,3,11])
offsets = np.array([10,15,17,1,0,1,0])

# derived settings
timings = np.arange(1,len(wheels)+1)

# CX = R(mod M)
def cbaToDoEuclid(C,M,R):
	X = 0
	while (C*X)%M != R:
		X+=1
	return X

mods = np.mod(np.negative(timings+offsets),wheels)

# do chinese remainder
factors = np.divide(np.prod(wheels),wheels)

# find scalars for each sum
scalars = [cbaToDoEuclid(C,M,R) for C,M,R in zip(factors,wheels,mods)]

# return minimum steps
print "STEPS: ", np.mod(np.sum(scalars*factors),np.prod(wheels))
