#!/usr/bin/env python3

import os
import sys
from collections import Counter
from collections import defaultdict

args=sys.argv[1:]

if len(args) != 2:
    print('Usage: {} LEN STR'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

if not args[0].isdigit():
    print('Kmer size "{}" is not a number'.format(args[0]))
    sys.exit(1)

kmer_size = int(args[0])
if kmer_size < 1:
    print('Kmer size "{}" must be > 0'.format(kmer_size))
    sys.exit(1)

dna = args[1]
nkmers = len(dna) - kmer_size + 1

if nkmers < 1:
    print('There are no {}-mers in "{}"'.format(args[0], args[1]))
    sys.exit(1) 

inp=defaultdict(int)

for i in range(nkmers):
    kmer = dna[i:i+kmer_size]
    inp[kmer] += 1

print(dna)
for key, value in sorted(inp.items()):
    print(key, value)
