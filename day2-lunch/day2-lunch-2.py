#!/usr/bin/env python3
def change_ID(map_id, c_tab, replace = 'no'):
    #read in file and lines
    map_id_f = open(map_id, 'r')
    map_id_d = {}
    for line in map_id_f:
        fly_id_up = line.split()
        map_id_d.setdefault(fly_id_up[0], fly_id_up[1])
    map_id_f.close()

    new_rseq = []
    rseq = open(c_tab, 'r')
    for line in rseq:
        rseq_split = line.split()
        if rseq_split[0] == 't_id':
            continue
        elif map_id_d.get(rseq_split[8], -1) == -1 and replace == 'no':
            continue
        elif map_id_d.get(rseq_split[8], -1) == -1 and replace == 'yes':
            rseq_split[8] = 'NA'
            new_rseq.append('\t'.join(map(str, rseq_split)))
        else:
            rseq_split[8] = map_id_d.get(rseq_split[8])
            new_rseq.append('\t'.join(map(str, rseq_split)))
    rseq.close()

    np.savetxt('day2-lunch-2.out', new_rseq, fmt="%s")


if __name__== "__main__":
    import sys
    import numpy as np

    change_ID(sys.argv[1], sys.argv[2], sys.argv[3])
