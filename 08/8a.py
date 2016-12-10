import numpy as np
import sys
import os
import time

SCREEN = np.zeros((6,50))

def rect(screen,w,h):
	screen[0:h,0] = 1
	screen[0:h,w-1] = 1
	screen[0,0:w] = 1
	screen[h-1,0:w] = 1

def rotate_column(screen,col,n):
	data = screen[:,col]
	data = np.roll(data,n)
	screen[:,col] = data

def rotate_row(screen,row,n):
	data = screen[row,:]
	data = np.roll(data,n)
	screen[row,:] = data

def print_screen(screen,char='#'):
	sys.stdout.write('\n')
	for row in screen:
		for cell in row:
			if cell:
				sys.stdout.write(char)
			else:
				sys.stdout.write('.')
		sys.stdout.write('\n')
	sys.stdout.write('\n')

with open('instructions.txt') as f:
	for l in f:
		data = l.strip().split(' ')

		if data[0] == 'rect':
			w,h = data[1].split('x')
			rect(SCREEN,int(w),int(h))

		elif data[0] == 'rotate':
			if data[1] == 'column':
				rotate_column(SCREEN,int(data[2][2:]),int(data[4]))
			else:
				rotate_row(SCREEN,int(data[2][2:]),int(data[4]))

		else:
			pass
		os.system('clear')
		print l
		print_screen(SCREEN)
		time.sleep(0.1)

	print np.sum(SCREEN)
