#!/usr/bin/env python3

import re
import statistics
#read in file
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
#check and remove any headers and add to count if alignment on chromosome 2L is between base 10000 and 20000
count = 0
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        split_line = lines.split('\t')
        if split_line[2] == '2L' and int(split_line[3]) >= 10000 and int(split_line[3]) <= 20000:
            count += 1 
#print count
print('There are ' + str(count) + ' reads that start their alignment on chromosome 2L between base 10000 and 20000')