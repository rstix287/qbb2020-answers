#!/usr/bin/env python3

# function to replace rseq data with uniprot ID 
def change_ID(map_id, c_tab, replace = 'no'):
    #read in map_id file and lines and creates dictionary
    map_id_f = open(map_id, 'r')
    map_id_d = {}
    #adds each fly id as key and uniprot id as the value to dictionary
    for line in map_id_f:
        fly_id_up = line.split()
        map_id_d.setdefault(fly_id_up[0], fly_id_up[1])
    map_id_f.close()

    #reads c_tab file
    new_rseq = []
    rseq = open(c_tab, 'r')
    for line in rseq:
        rseq_split = line.split()
        # if header puts in file
        if rseq_split[0] == 't_id':
            rseq_split[8] = 'UniProt_id'
            new_rseq.append('\t'.join(map(str, rseq_split)))
        # if specified not to replace if fly id isnt found skips
        elif map_id_d.get(rseq_split[8], -1) == -1 and replace == 'no':
            continue
        # if specified to replace if fly id not found, replaces with 'NA'
        elif map_id_d.get(rseq_split[8], -1) == -1 and replace == 'yes':
            rseq_split[8] = 'NA'
            new_rseq.append('\t'.join(map(str, rseq_split)))
        # inputs corresponding UniProt id of fly id in rseq data
        else:
            rseq_split[8] = map_id_d.get(rseq_split[8])
            new_rseq.append('\t'.join(map(str, rseq_split)))
    rseq.close()
    # prints rseq data
    np.savetxt('day2-lunch-2.out', new_rseq[0:100], fmt="%s")


if __name__== "__main__":
    import sys
    import numpy as np
    if len(sys.argv) == 4 and sys.argv[3] == 'yes':
        change_ID(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        change_ID(sys.argv[1], sys.argv[2])
