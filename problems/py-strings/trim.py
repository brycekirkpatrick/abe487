#!/usr/bin/env python3

import sys
import os

args = sys.argv[1:]

if len(args) < 1:
	print('Usage: {} INPUT [LEN]'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

file = args[0]
seqlen = int(args[1]) if len(args) > 1 else 5 #default sequence length

lines=[]

if os.path.isfile(file):	
	lines=open(file).read().splitlines()
else:
	lines=[file]	

for line in lines:
	print(line[:seqlen])

