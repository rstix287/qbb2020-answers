#!/usr/bin/env python3

import re
import statistics
#read in files
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
#check and remove any headers and pulls alignment scores
match = 0
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        for iter in lines.split('\t'):
            if re.match('^NM', iter):
                match_score = iter.split(':')
                if int(match_score[2]) == 0:
                    match += 1
#count perfect alignments
print('There are ' + str(match) + ' that match perfectly to the genome')