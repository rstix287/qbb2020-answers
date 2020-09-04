#!/usr/bin/env python3
# function that takes in 3 arguments and reports matches to kmers from targer sequence
def kmer_matcher(target, query, match_file):
    #read in match file
    match = open(match_file, 'r')
    match_log = {}
    #create dictionary of start positions for target and query sequences
    for line in match:
        line_split = line.split()
        match_log.setdefault(line_split[0], [])
        match_log[line_split[0]].append((int(line_split[1]), int(line_split[2])))
    #read target sequence
    read_target = FASTAReader(open(target))
    arr_seq = []
    # for each target sequence read query sequence and check if dictionary contains target sequence
    # id, then append id to overarching array. 
    for seq_idt, sequencet in read_target:
        read_query = FASTAReader(open(query))
        for seq_idq, sequenceq in read_query:
            if match_log.get(seq_idt, -1) == -1:
                continue
            else:
               arr_seq.append(seq_idt)
               arr_id_seq = []
               # for each starting index from target and query get 11 base sequence and while 
               # query and target are equal, increase length by 1 then append when while loop breaks
               for tar_i, quer_i in match_log.get(seq_idt):
                   len_seq = 11
                   tar_seq = sequencet[tar_i: tar_i + len_seq].upper()
                   quer_seq = sequenceq[quer_i: quer_i + len_seq].upper()
                   while tar_seq == quer_seq:
                       len_seq += 1
                       tar_seq = sequencet[tar_i: tar_i + len_seq].upper()
                       quer_seq = sequenceq[quer_i: quer_i + len_seq].upper()
                   arr_id_seq.append(sequencet[tar_i: tar_i + len_seq - 1].upper())
               # sort by length and add to sequence specific array
               arr_id_seq.sort(key=len, reverse=True)
               arr_seq.extend(arr_id_seq)
    # print array as column
    np.savetxt('kmer_match_extender.out', arr_seq, fmt="%s")



if __name__ == '__main__':
    import sys
    import numpy as np
    from fasta_iterator_class import FASTAReader
    kmer_matcher(sys.argv[1], sys.argv[2], sys.argv[3])
