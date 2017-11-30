#!/usr/bin/env python3

import argparse
import os
import sys
#from Bio import SearchIO

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Parse BLAST tab')
    parser.add_argument('positional', metavar='file', help='BLAST tab output')
    parser.add_argument('-p', '--pct_id', help='Percent identity',
                        metavar='float', type=float, default=0)
    parser.add_argument('-e', '--evalue', help='',
                        metavar='float', type=float, default=None)
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    file = args.positional
    pct_id = args.pct_id
    evalue = args.evalue

#    info= SearchIO.read(file, 'blast-tab')
#    line = 'qid\tsid\t83.99\t37\t14\t15\t1\t147\t1\t149\t0.0\t219\n'    
#    for stuff in info:
#        print(Hsp(line).pident)
#    hsp=Hsp(line)
    flds = 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore'.split()
    for line in open(file):
        row=dict(zip(flds , line.split('\t')))
        if float(row['pident']) < pct_id:
            continue   
        if evalue is not None and float(row['evalue']) > evalue: 
            continue
        print('\t'.join([row['qseqid'], row['sseqid'], row['pident'], row['evalue']]))
         
#        print('ok')

# --------------------------------------------------
if __name__ == '__main__':
    main()
