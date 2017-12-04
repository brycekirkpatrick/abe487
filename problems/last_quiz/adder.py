#!/usr/bin/env python3

import sys
import os

args=sys.argv[1:]

if len(args)!= 2:
    print('Usage: adder.py ARG1 ARG2')
    sys.exit(1)
if type(args[0]) != type(args[1]):
    print('Cannot combine number and string')

if args[0].isdigit() and args[1].isdigit():
    output=int(args[0])+int(args[1])
    print(output)
else:
    print("{} {}".format(args[0], args[1]))

