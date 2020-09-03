#!/usr/bin/env python3
# function that takes in 3 arguments and reports matches to kmers from targer sequence
def kmer_matcher(target, query, k):
    #read target sequences
    read_target = FASTAReader(open(target))
    #set up beginning of dictionary
    kmers = {}
    #for each seq_id and sequence read and log kmer in dictionary as tuples where kmer is key
    #and lists of tuples of seq_id and location in value
    for seq_id, sequence in read_target:
        for i in range(0, len(sequence) - k + 1):
            kmer = sequence[i:i + k].upper()
            kmers.setdefault(kmer, [])
            kmers[kmer].append((seq_id, i))
    #opens file to write out kmer matches to
    f = open('kmer_matcher.out', 'w')
    #reads query sequence
    read_query = FASTAReader(open(query))
    for seq_idq, sequenceq in read_query:
        #for each kmer in query sequence checks if its in the dictionary
        #if not it continues, othewise it writes out target_sequence id, target start, query start and kmer
        for itera in range(0, len(sequenceq) - k + 1):
            kmerq = sequenceq[itera:itera + k].upper() 
            if kmers.get(kmerq, -1) == -1:
                continue
            else:
                target_id = kmers.get(kmerq)
                for seq_id, start in target_id:
                    f.write('{}\t{}\t{}\t{}\n'.format(seq_id, start, itera, kmerq))
    f.close()


if __name__ == '__main__':
    import sys
    from fasta_iterator_class import FASTAReader
    kmer_matcher(sys.argv[1], sys.argv[2], int(sys.argv[3]))
