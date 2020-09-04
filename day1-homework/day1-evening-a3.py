#!/usr/bin/env python3

import re
import statistics
#read in files
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
#check and remove any headers and determines number of insertions and deletions
count_i1 = 0
count_i2 = 0
count_i3 = 0
count_i4 = 0
count_ig4 = 0
count_d1 = 0
count_d2 = 0
count_d3 = 0
count_d4 = 0
count_dg4 = 0
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        cigar = lines.split('\t')[5]
        op = re.split('[0-9]', cigar)
        bam = re.split('[A-Z]|=', cigar)
        while("" in op):
            op.remove("")
        while("" in bam):
            bam.remove("")
        for oper in range(0, len(op)):
            if op[oper] == 'I' and int(bam[oper]) == 1:
                count_i1 += 1
            elif op[oper] == 'I' and int(bam[oper]) == 2:
                count_i2 += 1
            elif op[oper] == 'I' and int(bam[oper]) == 3:
                count_i3 += 1
            elif op[oper] == 'I' and int(bam[oper]) == 4:
                count_i4 += 1
            elif op[oper] =='I' and int(bam[oper]) > 4:
                count_ig4 += 1
            elif op[oper] == 'D' and int(bam[oper]) == 1:
                count_d1 += 1
            elif op[oper] == 'D' and int(bam[oper]) == 2:
                count_d2 += 1
            elif op[oper] == 'D' and int(bam[oper]) == 3:
                count_d3 += 1
            elif op[oper] == 'D' and int(bam[oper]) == 4:
                count_d4 += 1
            elif op[oper] =='D' and int(bam[oper]) > 4:
                count_dg4 += 1
print('There are: \n{0} insertions of length 1\n{1} insertions of length 2\n{2} insertions of length 3\n{3} insertions of length 4\n{4} insertions of length greater than 4\n{5} deletions of length 1\n{6} deletions of length 2\n{7} deletions of length 3\n{8} deletions of length 4\n{9} deletions of length greater than 4\n'.format(count_i1, count_i2, count_i3, count_i4, count_ig4, count_d1, count_d2, count_d3, count_d4, count_dg4))