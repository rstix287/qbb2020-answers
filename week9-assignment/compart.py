#!/usr/bin/env python2
import hifive
import matplotlib.pyplot as plt
import numpy as np
# read in data
hic=hifive.HiC('./project.fend', 'r')
Comp = hifive.hic_domains.Compartment(hic, 100000, chroms=['chr13'], out_fname='tmp.hdf5')
Comp.write_eigen_scores('hic_comp.bed')

# Plot compartment scores
X = Comp.positions['chr13']
Y = Comp.eigenv['chr13']
fig, ax = plt.subplots()
ax.plot(X, Y)
ax.set_title("Compartment Scores Chromosome 13", fontsize = 16)
ax.set_xlabel("Genomic Positions", fontsize = 16)
ax.set_ylabel("Compartment Score", fontsize = 16)
plt.savefig('compartment.png')
