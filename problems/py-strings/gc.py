#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dna = args[0]

#print('DNA is "{}"'.format(dna))

tot=len(dna)
i = 0
for letter in dna:
	if letter in 'CG':
		i += 1	

print('{}% GC'.format(int(i*100/tot)))
	

		
