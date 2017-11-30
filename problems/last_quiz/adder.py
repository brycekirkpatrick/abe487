#!/usr/bin/env python3

import sys
import os

args=sys.argv[1:]

if len(args)!= 2:
    print('Usage: adder.py ARG1 ARG2')
    sys.exit(1)

if type(args[0]) == type(args[1]):
    if type(args[0]) and type(args[1]) == int:
        output=int(args[0])+int(args[1])
        print(output)
    else:
        print(args[0]+args[1])
if type(args[0]) != type(args[1]):
    print('Cannot combine number and string') 
    
#else:
#    strings=args[0] + args[1]
#    print(strings)
