#!/usr/bin/env python2
import hifive
import matplotlib.pyplot as plt
import numpy as np
# read in data
hic=hifive.HiC('./project.fend', 'r')
data=hic.cis_heatmap('chr13', 1000000, datatype='fend', arraytype='full', diagonalincluded=True)
# Calculate corrected enrichment
ind_true = np.where(data[:,:,0:2]>0)
enrichment = data[ind_true[0], ind_true[1], 0]/ data[ind_true[0], ind_true[1], 1]
# create 2D array to input data to for plotting
enrich_matrix = np.zeros((1193, 1193))
for x in range(len(enrichment)):
    enrich_matrix[ind_true[0][x]][ind_true[1][x]] = np.log(enrichment[x])

# plot heatmap
fig, ax = plt.subplots()
im = ax.imshow(enrich_matrix, cmap = "Reds")
cbar = ax.figure.colorbar(im, ax=ax)
cbar.set_label("Log corrected enrichment scores")
ax.set_xlabel("Chromosome 13 1Mb bin", fontsize = 16)
ax.set_ylabel("Chromosome 13 1Mb bin", fontsize = 16)
ax.set_title("C13 log of corrected enrichment scores", fontsize = 16)
plt.savefig('Chrom13_heatmap.png')
