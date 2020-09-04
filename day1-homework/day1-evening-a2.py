#!/usr/bin/env python3

import re
import statistics
#read in files
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
#check and remove any headers and determine if qual score is greater than 30
count = 0
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        qual = lines.split('\t')[10]
        scores = []
        for char in qual:
            scores.append(ord(char)-33)
        if statistics.mean(scores) > 30:
            count += 1
#print count
print(str(count) + ' reads have an average quality score > 30')