#!/bin/bash

for i in 09 11 23 24 27 31 35 39 62 63
do
    bwa mem -R "@RG\tID:A01_$i\tSM:A01_$i" -o A01_$i.sam sacCer3.fa A01_$i.fastq
done 