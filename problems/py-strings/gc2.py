#!/usr/bin/env python3

import os
import sys

args=sys.argv #use isfile() to test for file
file=args[1]
if not os.path.isfile(file):
	print('"{}" is not a file'.format(os.path.basename(args[1])))
	sys.exit(1)
else:
	i = 0
	t = 0
	for line in open(file): #should probably use open(file).readlines for this
		t += 1
		if t == 1:
			i = 0
			t = 0
		for letter in line.upper():
			if letter in 'GC':
				i += 1
		print(i*100/(len(line.upper())-1))
