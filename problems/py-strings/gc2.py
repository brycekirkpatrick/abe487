#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]
if not os.path.isfile(file):
    print('"{}" is not a file'.format(os.path.basename(file)))
    sys.exit(1)

for line in open(file): #should probably use open(file).readlines for this
    i = 0
    for letter in line.upper():
        if letter in 'GC':
            i += 1
    print(int(i*100/(len(line.upper())-1)))
