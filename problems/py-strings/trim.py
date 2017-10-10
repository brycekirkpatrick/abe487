#!/usr/bin/env python3

import sys
import os

args = sys.argv[1:]

if len(args) < 1:
	print('Usage: {} INPUT [LEN]'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

file = args[0]
seqlen = int(args[1]) if len(args) > 1 else 5 #default sequence length

#print('file "{}" seqlen "{}"'.format(file, seqlen))
lines=[]

if os.path.isfile(file):	
	lines=open(file).read().splitlines()
else:
	lines=[file]	

for line in lines:
	print(line[:seqlen])

#if not os.path.isfile(file):
# if file.isstring():
#  for line in 'CGTA'
#  print('{}'.format(seglen))
#else:
# for line in open(file):
#
##core part of code: for characters in string/file print that string up to arg[2]
