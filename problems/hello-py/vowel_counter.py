#!/usr/bin/env python3

import os
import sys

args = sys.argv

if len(args) < 2:
	print('Usage: {} STRING'.format(os.path.basename(args[0])))
	sys.exit(1)
else:
	z=0  #not using i, worrried I will get the vowels and the count confused
	for letter in args[1]: 
		if letter in 'aeiou':
			z+=1
	if z == 1:
		print('There is 1 vowel in "{}."'.format(args[1]))
	elif z > 1:
		print('There are {} vowels in "{}."'.format(z,args[1]))
	else:
		print('There are 0 vowels in "{}."'.format(args[1]))
