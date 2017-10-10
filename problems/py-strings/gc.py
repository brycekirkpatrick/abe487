#!/usr/bin/env python3

import sys
import os
args=sys.argv

tot=len(args[1])
i = 0
for letter in args[1]:
	if letter in 'CG':
		i += 1	
print('{}% GC'.format(i*100/tot))
	

		
