import numpy as np
valid_count = 0

with open("triangles.txt") as f:
	# for l in f:
	# 	print l
	# 	edges = [int(x.strip()) for x in l.split()]
	# 	edges.sort()
	# 	print edges
	# 	if sum(edges[:2])>edges[2]:
	# 		valid_count+=1

	# print valid_count
	flag = True
	while flag:
		trip = []
		for i in range(3):
			l = f.readline()
			if not l:
				flag = False #EOF
				break
			trip.append([int(x.strip()) for x in l.split()])

		trip = np.transpose(trip)

		for t in trip:
			t.sort()
			if sum(t[:2])>t[2]:
				valid_count+=1

	print valid_count