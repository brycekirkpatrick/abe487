#!/bin/bash

#PBS -W group_list=bh_class
#PBS -q windfall
#PBS -l select=1:ncpus=6:mem=12gb
#PBS -l walltime=48:00:00
#PBS -l cput=48:00:00
#PBS -M brycekirkpatrick@email.arizona.edu
#PBS -m bea

module load fastx

echo “my job_id is: ${PBS_JOBID}”
FASTQ_DIR="/rsgrps/bh_class/brycekirkpatrick/fastq"

i=0
#for FILE in "$@"; do
for FILE in $FASTQ_DIR/*.fastq; do
    let i++
    BASENAME=$(basename "$FILE")
    FA="${FILE%.fastq}.fa"
    printf "%3d: %s -> %s\n" $i $BASENAME $FA

    START=12
    END=300

    #[[ $BASENAME == "SRR059952_2.fastq" ]] && START=8
    #[[ $BASENAME == "SRR059952_2.fastq" ]] && END=200

    #if [[ $FILE == "SRR059952_2.fastq" ]]; then
    #    START=8
    #fi

    cat $FILE | fastx_trimmer -f $START -l $END | \
      fastq_quality_filter -q 20 -p 80 | \
      fastx_clipper -l 70 | \
      fastx_collapser > $FA
done

echo "Done."
exit
