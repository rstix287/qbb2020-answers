#!/bin/bash

for SAMPLE in 83_1 83_2 86_1 86_2 88_1 88_2 89_1 89_2 90_1 90_2 93_1 93_2 94_1 94_2 97_1 97_2
 do
   bwa mem -R "@RG\tID:Sample1\tSM:Sample1" -o ${SAMPLE}.sam week13_data/assembly.fasta week13_data/READS/SRR4921${SAMPLE}.fastq
done