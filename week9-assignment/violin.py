#!/usr/bin/env python2
import matplotlib.pyplot as plt
import numpy as np
# read in data
pos = np.genfromtxt('positive_WT_fpkm.bed', usecols=4)
neg = np.genfromtxt('negative_WT_fpkm.bed', usecols=4)

# Plot compartment scores
fig, ax = plt.subplots()
part = ax.violinplot(pos, positions=[0], showmeans=False, showmedians=False, showextrema=False)
part2 = ax.violinplot(neg, positions=[1], showmeans=False, showmedians=False, showextrema=False)
ax.set_yscale('log')
ax.set_xticks([0, 1])
ax.set_xticklabels(['B-compartment (positive)', 'A-compartment (negative)'])
for pc in part['bodies']:
    pc.set_facecolor('violet')
    pc.set_edgecolor('blue')
    pc.set_alpha(1)

for pc in part2['bodies']:
    pc.set_facecolor('blue')
    pc.set_edgecolor('violet')
    pc.set_alpha(1)

ax.set_title("Chromosome 13 Gene Expression", fontsize = 16)
ax.set_ylabel("Gene Expression FPKM", fontsize = 16)
ax.set_xlabel("Compartment Score", fontsize = 16)
plt.savefig('expression_violin.png')
