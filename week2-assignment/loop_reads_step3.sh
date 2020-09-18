#!/bin/bash

for i in 09 11 23 24 27 31 35 39 62 63
do
    samtools view -S -b A01_$i.sam > A01_$i.bam
    samtools sort A01_$i.bam  -O BAM -o sorted_A01_$i.bam 
done
