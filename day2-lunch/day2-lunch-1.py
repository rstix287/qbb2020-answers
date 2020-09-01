#!/usr/bin/env python3

import numpy as np

#read in file and lines
map_file = []
fly = open('fly.txt', 'r')
for line in fly:
    if 'DROME' in line and 'FBgn' in line:
        data = line.split()
        map_file.append(data[-1] + '\t' + data[-2])
fly.close()

np.savetxt('day2-lunch-1.out', map_file, fmt="%s")

