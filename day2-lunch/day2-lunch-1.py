#!/usr/bin/env python3

import numpy as np

#read in file and lines of file from fly.txt
map_file = []
fly = open('fly.txt', 'r')
# checks if 'DROME' and 'FBgn' are in the line,
# if so, it appends the fly id and the uniprot id (tab separated) to array
for line in fly:
    if 'DROME' in line and 'FBgn' in line:
        data = line.split()
        map_file.append(data[-1] + '\t' + data[-2])
fly.close()
# writes out array to file
np.savetxt('day2-lunch-1.out', map_file, fmt="%s")

