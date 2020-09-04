#!/usr/bin/env python3

import re
import statistics
#read in files
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
#check and remove any headers and append MAPQ scores to mapq array
mapq = []
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        mapq.append(float(lines.split('\t')[4]))
#average MAPQ
print('The average MAPQ score is: ' + str(statistics.mean(mapq)))