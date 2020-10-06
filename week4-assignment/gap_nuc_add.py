#!/usr/bin/env python3

def aa_conversion(aa_file, nuc_file):
    #read aa_file and nuc_file sequences
    aa_seq = FASTAReader(open(aa_file))
    nuc_seq = FASTAReader(open(nuc_file))
    #set up dictionary of sequences
    seq_dict = {}
    #create dictionary of sequences per id
    for seq_id, sequence in nuc_seq:
        seq_dict.setdefault(seq_id.split(" ")[0], [sequence])
    for seq_id, sequence in aa_seq:
        seq_dict[seq_id.split(" ")[0][:-2]].append(sequence)

    #loops through dictionary and creates new sequence
    for key, item in seq_dict.items():
        nuc_og = item[0]
        aa = item[1]
        nuc_new = ''
        counter_og = 0
        for char in aa:
            if char == '-':
                nuc_new = nuc_new + '---'
            else:
                nuc_new = nuc_new + nuc_og[counter_og:counter_og+3]
                counter_og += 3
        seq_dict[key].append(nuc_new)
    return seq_dict


def ds_dn_determination(seq_dict):
    # codon table used to determine AA comparison for ds and dn
    codontable = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T','AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K','AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R','CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L','CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P','CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q','CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R','GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V','GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A','GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E','GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G','TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S','TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L','TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_','TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    # pull the aligned query sequence from dictionary 
    query_seq = seq_dict["NC_001563.2"][2]
    # set up initial arrays of zeros to be adding values to as it goes through 1000 aligned sequences
    dN = np.zeros(int(len(query_seq)/3), dtype=int)
    dS = np.zeros(int(len(query_seq)/3), dtype=int)
    # for each of 1000 sequences pulls aligned seuqnece pulls the aligned sequence
    for key, item in seq_dict.items():
        nuc_aln = item[2]
        # for each codon in the sequence/query sequence checks if they are a gap (skips) or if equal (skips)
        # then makes sure that the codon is in the codon table --> isnt YGT for example
        # finally converts both query and sequence codons to AA and compares them to add to dS and dN arrays
        for codon in range(0, len(nuc_aln), 3):
            if query_seq[codon:codon+3] == '---':
                continue
            elif nuc_aln[codon:codon+3] == '---':
                continue
            elif query_seq[codon:codon+3] == nuc_aln[codon:codon+3]:
                continue
            if nuc_aln[codon:codon+3] in codontable:
                query_aa = codontable[query_seq[codon:codon+3]]
                aln_aa = codontable[nuc_aln[codon:codon+3]]
                index = int(codon/3)
                if query_aa == aln_aa:
                    dS[index] += 1
                else:
                    dN[index] += 1
    indx_del = []
    # checking for if dS and/or dN are zero and removing any that are 
    for codon in range(0, len(dN)):
        if dN[codon] == 0 or dS[codon] == 0:
            indx_del.append(codon)
    dN = np.delete(dN, indx_del)
    dS = np.delete(dS, indx_del)
    # return dN and dS arrays
    return dN, dS


if __name__ == '__main__':
    import sys
    import numpy as np
    from fasta_iterator_class import FASTAReader
    # creating a sequence dictionary and aligning DNA sequence based on protein alignement
    seq_dict = aa_conversion(sys.argv[1], sys.argv[2])
    # determining dN and dS compared to query sequence
    dN, dS = ds_dn_determination(seq_dict)
    # writing out dN and dS arrays to files
    np.savetxt("dN.txt", dN)
    np.savetxt("dS.txt", dS)
