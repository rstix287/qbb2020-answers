#!/usr/bin/env python3
#load modules
import numpy as np
import math

#read in positions of interest
poi = np.genfromtxt('/Users/cmdb/qbb2020-answers/day4-lunch/day3_100_positions.txt', dtype=np.dtype(str))
gene = []
iterations = []
for pos_int in range(0, len(poi)):

    #read in gtf file
    gtf = open('/Users/cmdb/qbb2020-answers/day4-lunch/BDGP6.Ensembl.81.gtf', 'r')
    #set header for parsed data, will be removed later
    arr_prot_cod_gene = [['gene', 'start', 'stop']]
    # parse input lines to make sure chromosome 3R, gene and protein coding and put into 2D array
    for line in gtf:
        line_split = line.rstrip().split()
        if poi[pos_int][0] in line_split[0] and 'gene' in line_split[2] and 'protein_coding' in line_split[-1]:
            arr_prot_cod_gene = np.vstack((arr_prot_cod_gene, [line_split[13].strip('"|;'), line_split[3], line_split[4]]))
    gtf.close()
    #set up starting variables for binary search: start, stop, count, position, and remove header of array
    arr_prot_cod_gene = arr_prot_cod_gene[1:len(arr_prot_cod_gene)][:]
    start = 0
    stop = len(arr_prot_cod_gene)
    count = 0
    dist = 0
    position = int(poi[pos_int][1])
    #while loop for binary search
    while (start != stop):
        # getting the halfway point between start stop
        mid = math.floor((((stop - start)/2)+start))
        # compares if the halfway point in the array interval is less than, greater than, 
        # including or equal to the position and changes start or stop -
        if position < int(arr_prot_cod_gene[mid][1]):
            stop = mid
        elif position > int(arr_prot_cod_gene[mid][2]):
            start = mid
        elif position >= int(arr_prot_cod_gene[mid][1]) and position <= int(arr_prot_cod_gene[mid][2]):
            start = mid
            stop = mid
        #if the start and stop i.e. low and high are one away it could endlessly loop due to floor function
        #compares the minimum distance to each of the two genes to determine which is closest
        if (stop-start) == 1:
            stop_min = min(abs(int(arr_prot_cod_gene[stop][1])-position), abs(int(arr_prot_cod_gene[stop][2])-position))
            start_min = min(abs(int(arr_prot_cod_gene[start][1])-position), abs(int(arr_prot_cod_gene[start][2])-position))
            if stop_min < start_min:
                dist = stop_min
                start = stop
            else: 
                dist = start_min
                stop = start
        #count interations
        count += 1
    gene.append([arr_prot_cod_gene[start][0]])
    iterations.append([str(count)])
poi = np.hstack((poi, gene))
poi = np.hstack((poi, iterations))
header = ['CHROM', 'PositionOfIntrest', 'NearestGene', 'Iterations']
poi = np.vstack((header, poi))
np.savetxt('day4-lunch_4.out', poi, fmt="%s")
