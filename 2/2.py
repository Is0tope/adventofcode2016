
import numpy as np

D = {'L' : np.array([-1,0]),
	'R' : np.array([1,0]),
	'D' : np.array([0,1]),
	'U' : np.array([0,-1])}

#pad = 1+np.arange(9).reshape(3,3)
pad = np.array([[' ',' ','1',' ',' '],
			   [' ','2','3','4',' '],
			   ['5','6','7','8','9'],
			   [' ','A','B','C',' '],
			   [' ',' ','D',' ',' ']])

with open("directions.txt") as f:
	# start at 5
	coords = np.array([0,2])
	for l in f:
		for c in l.strip():
			new_coords = coords + D[c]
			# filter
			# if distance is two away from center, then invalid move
			if np.sum(np.abs(new_coords - np.array([2,2]))) > 2:
				continue
			coords = new_coords
			coords = np.maximum(coords,np.array([0,0]))
			coords = np.minimum(coords,np.array([4,4]))
		print pad[coords[1]][coords[0]]
			