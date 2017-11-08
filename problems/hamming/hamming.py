#!/usr/bin/env python3
import sys
import os

args=sys.argv[1:]

if len(args) < 1:
    print("Usage: requires two strings")
    sys.exit(1)
input1=args[0]
input2=args[1]

print(input1, input2)
length1=len(input1)
length2=len(input2)
i=0
if length1 < length2:
    i = length2 - length1
if length1 > length2:
    i = length1 - length2
#print(i)

for char, letter in zip(input1, input2):
#    print(char,letter)
    if char != letter:
        i=i+1
print(i)

