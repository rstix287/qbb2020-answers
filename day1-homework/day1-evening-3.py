#!/usr/bin/env python3

import re
#read in files
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
#check and remove any headers
align = []
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        align.append(lines)
#pull the first 10 alignments, split and print chromosome it aligns to
for iter in range(0,10):
    print(align[iter].split('\t')[2])