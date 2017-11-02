#!/usr/bin/env python3

import argparse
import os
import sys
from Bio import SeqIO
args=sys.argv[1:]

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='FASTA read trimmer')
    parser.add_argument('file', metavar='file', help='FASTA file')
    parser.add_argument('-s', '--start', help='Start position',
                        metavar='int', type=int, default=0)
    parser.add_argument('-e', '--end', help='End position', 
                        metavar='int', type=int, default=None)
    parser.add_argument('-m', '--min', help='Minimum length',
                        metavar='int', type=int, default=0)
    parser.add_argument('-o', '--outfile', help='Output file',
                        metavar='str', type=str, default="") # need to change
    return parser.parse_args()
#need arguemnt for file input here, not sure how to do....
# --------------------------------------------------
def main():
    args = get_args()
    out = args.outfile
    start = args.start
    end = args.end

    min_arg = args.min
    file = args.file

    if start > 0:
        start = start - 1
    if len(out)	== 0:
       	out= file + '.trimmed'
    
    out_fh = open(out, 'w')
    
    num_taken = 0
    with open(file) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seq = str(record.seq[start:end])
            if len(seq) >= min_arg:
                num_taken += 1
                out_fh.write('\n'.join(['>' + record.id, seq, '']))
    print('Wrote {} sequence{} to "{}"'.format(num_taken,''  if num_taken == 1 else 's', out))


#    good_seq=[]
#    for record in SeqIO.parse(file, "fasta"):#opens the entire file,just need seq
#        if len(record.seq[start:end]) >  min_arg:
#            print(record.seq[start:end]) 
# good_seq.append(record.seq[start:end])
#    if out is "":
#        out=[file] + ".trimmed"
#    SeqIO.write(good_seq, out, 'fasta')


#if outfile ="" then name [inputfile].trimmed
# --------------------------------------------------
if __name__ == '__main__':
    main()

