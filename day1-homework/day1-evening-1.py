#!/usr/bin/env python3

import re

#read in file and lines
sam = open('/Users/cmdb/qbb2020-answers/day1-evening/SRR072893.sam', 'r')
whole_sam = sam.readlines()
align = []
# iterate through and check for header/make new array without header
for lines in whole_sam:
    if re.match('^@', lines):
        continue
    else:
        align.append(lines)

#print number of alignments in file
print('The number of alignments in this file is: ' + str(len(align)))