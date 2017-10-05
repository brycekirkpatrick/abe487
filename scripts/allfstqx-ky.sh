#!/bin/bash

i=0
for FILE in "$@"; do
    let i++
    BASENAME=$(basename "$FILE")
    FA="${BASENAME%.fastq}.fa"
    printf "%3d: %s -> %s\n" $i $BASENAME $FA

    START=12
    [[ $BASENAME == "SRR059952_2.fastq" ]] && START=8
    
    END=300
    [[ $BASENAME == "SRR059952_2.fastq" ]] && END=200

    if [[ $FILE == "SRR059952_2.fastq" ]]; then
        START=8
    fi

    #fastx_trimmer -f $START -l $END $FILE | \
    #  fastq_quality_filter -q 20 -p 80 | \
    #  fastx_clipper -l 70 | \
    #  fastx_collapser > $FA
done

echo "Done."
exit
