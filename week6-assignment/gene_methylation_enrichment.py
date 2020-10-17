#!/usr/bin/env python3

def verify_gap1(file_name):
    #verify that each methyl site in bedgraph files represents 1 nucleotide site, not multiple in sequnce
    #numpy read in columns of start and stop and verifys there is only a difference of 1 between start and stop
    # if not it will print out a message
    meth_site = np.genfromtxt(file_name, usecols=(1), skip_header=1)
    next_nuc = np.genfromtxt(file_name, usecols=(2), skip_header=1)
    for incr in range(0, len(meth_site)):
        if (meth_site[incr] + 1) != next_nuc[incr]:
            print("There is more than one methylation site in this line. Start coordinate: " + meth_site[incr])


def bedgraph(e4, e5):
    # read in E4 and E5.5 bedgraph and take out zeros in either and makes a 2D list of methyl sites in both E4 and E5.5
    # 2D list contains methyl signal for each site for E4 and E5.5 

    # only reads in the coordinate of methylation (verified each in bedgraph is only 1 already) and methyl signal for E4 and E5.5
    meth_site_e4 = np.genfromtxt(e4, usecols=((1,3)), skip_header=1)
    meth_site_e5 = np.genfromtxt(e5, usecols=((1,3)), skip_header=1)
    index_e4 = 0
    index_e5 = 0
    meth_site_fold_change = []
    # goes through each of the sites while the index using for each is less than the length
    while(index_e4 < len(meth_site_e4) and index_e5 < len(meth_site_e5)):
        # if either E4 or E5.5 is 0 then the index is increased for it 
        if meth_site_e5[index_e5][1] == 0:
            index_e5 += 1
        elif meth_site_e4[index_e4][1] == 0:
            index_e4 += 1
        # otherwise checks to see if the coordinates are the same between
        else:
            # if the coordinates are the same in E4 and E5.5 it will add the coordinate, and methyl signal for E4 and E5.5 at that coor to a 2D array
            # and then increment their index
            if meth_site_e4[index_e4][0] == meth_site_e5[index_e5][0]:
                meth_site_fold_change.append([int(meth_site_e4[index_e4][0]), meth_site_e5[index_e5][1], meth_site_e4[index_e4][1]])
                index_e4 += 1
                index_e5 += 1
            # Otherwise if one coordinate is smaller than the other, it will increment that one 
            elif meth_site_e4[index_e4][0] < meth_site_e5[index_e5][0]:
                index_e4 += 1
            else:
                index_e5 += 1

    # return 2D methyl coordinate and signals for E4 and E5.5
    return(meth_site_fold_change)

def gene_id(meth_arr, gene_file):
    # This reads in the bed file coordinates of each gene and gene ID
    # Since some gene IDs have mutiple coordinates a dictionary was created with a list of tuples of the start and stop coordinates for that gene
    # This dictionary is then compared to the 2D methyl coordinate and a new dictionary of gene IDs with a array containing the sum of E4, sum of E5
    # and count of things added for each methyl site within the gene coordinates is created
    # This is used to calculate fold change of mean methylation signal which is output to a file

    # read bed file and take coordinates and gene ID
    gene = np.genfromtxt(gene_file, usecols=((4,5,12)), dtype=str)

    # Create dictionary of list of tuples of start and stop coordinates for each gene ID
    gene_dict = {}
    for incr in range(0, len(gene)):
        gene_dict.setdefault(gene[incr][2], [])
        gene_dict[gene[incr][2]].append((int(gene[incr][0]), int(gene[incr][1])))

    # Compare gene id coordinates with coordinates of methyl sites and create dictionary of gene ID with sum of E4 and sum of E5 methyl sites, 
    # and count of things added
    gene_dict_fold_change = {}
    for key, item in gene_dict.items():
         gene_dict_fold_change.setdefault(key, [0.0, 0.0, 0])
         for incr in range(0, len(meth_arr)):
             for itera in item:
                 if itera[0] <= meth_arr[incr][0] and meth_arr[incr][0] <= itera[1]:
                     gene_dict_fold_change[key][0] += meth_arr[incr][1]
                     gene_dict_fold_change[key][1] += meth_arr[incr][2]
                     gene_dict_fold_change[key][2] += 1
                     break
         # if gene ID has no methyl sides remove from dictionary
         if gene_dict_fold_change[key][2] == 0:
             del gene_dict_fold_change[key]

    # make new 2D list with headers for output file and calculate the fold change from dictionary by averaging E4 and E5 methyl sites and then dividing
    # E5.5/E4
    gene_fc_out = [["gene_name", "relative_methylation_enrichment"]]
    for key, item in gene_dict_fold_change.items():
        gene_fc_out.append([key, (item[0]/item[2])/(item[1]/item[2])])

    # output to file
    np.savetxt("gene_methyl_enrichment.txt", gene_fc_out, fmt="%s", delimiter="\t")





if __name__ == '__main__':
    import sys
    import numpy as np
    # verify only one methyl site in each line in bedgraph files 
    verify_gap1(sys.argv[1])
    verify_gap1(sys.argv[2])
    # make 2D array of coordinate of methyl site and E4 and E5 methyl signals (only includes coordinates that have methyl signals at both E4 and E5.5)
    meth_site_fold_change = bedgraph(sys.argv[1], sys.argv[2])
    # Compares to genes and determines fold change of average methyl signal
    gene_id(meth_site_fold_change, sys.argv[3])

