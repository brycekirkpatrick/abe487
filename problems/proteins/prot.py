#!/usr/bin/env python3

import os
import sys
from collections import Counter
from collections import defaultdict

args=sys.argv[1:]

if len(args) != 1:
    print('Usage: {} SEQ'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

seq=args[0].upper()

RNA_codons = {}
with open('codons.rna', 'r') as codonsource: #found this code online and it is the only thing I can get to work
    for line in codonsource:
        flds = line.rstrip().split()
        RNA_codons[flds[0]] = flds[1]

#print(RNA_codons)
#sys.exit()

k=3
output=[]
for i in range(0,len(seq),k):
    RNA_3mer=seq[i:k+i]
    output.append(RNA_codons[RNA_3mer])
print(''.join(output))
sys.exit()
output=[]
sys.exit()
