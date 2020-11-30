#!/usr/bin/env python2
import pyBigWig
import matplotlib.pyplot as plt
import numpy as np

# read in data
bw = pyBigWig.open('data/WT_H3K27me3.bw')
pos_start = np.genfromtxt('positive_WT_fpkm.bed', usecols=1)
pos_end = np.genfromtxt('positive_WT_fpkm.bed', usecols=2)
pos_expression = np.genfromtxt('positive_WT_fpkm.bed', usecols=4)
neg_start = np.genfromtxt('negative_WT_fpkm.bed', usecols=1)
neg_end = np.genfromtxt('negative_WT_fpkm.bed', usecols=2)
neg_expression = np.genfromtxt('negative_WT_fpkm.bed', usecols=4)
pos_h3k27me3 = []
neg_h3k27me3 = []

# get H3K27me3 data corresponding to expression
for it in range(0, len(pos_start)):
    val = bw.stats('chr13', int(pos_start[it]), int(pos_end[it]), type='sum')
    if val is None:
        val = 0
    pos_h3k27me3.append(val)

for it in range(0, len(neg_start)):
    val = bw.stats('chr13', int(neg_start[it]), int(neg_end[it]), type='sum')
    if val is None:
        val = 0
    neg_h3k27me3.append(val) 

# Plot expression and H3K27me3
fig, ax = plt.subplots(2, sharex = True, sharey = True)
ax[0].scatter(pos_expression, pos_h3k27me3, alpha=0.5)
ax[1].scatter(neg_expression, neg_h3k27me3, alpha=0.5)
ax[0].set_title("B-Compartment", fontsize = 16)
ax[1].set_title("A-Compartment", fontsize = 16)
ax[0].set_xlabel("Expression FPKM", fontsize = 16)
ax[1].set_xlabel("Expression FPKM", fontsize = 16)
ax[0].set_ylabel("H3K27me3 Signal", fontsize = 16)
ax[1].set_ylabel("H3K27me3 Signal", fontsize = 16)
ax[0].set_yscale('log')
ax[1].set_yscale('log')
plt.tight_layout()
plt.savefig('expressionH3K27me3.png')
