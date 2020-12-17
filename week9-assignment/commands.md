# Setup and Load
$ conda create -n hifive hifive python=2 matplotlib bedtools pyBigWig 
$ conda activate hifive
$ wget "https://bx.bio.jhu.edu/data/cmdb-lab/3DGenomeData.tar.gz"
$ tar xzf 3DGenomeData.tar.gz 

# Normalizing hiC data
$ hifive fends -L genome/mm9.len --binned 100000 gen_part.fend

$ hifive hic-data -X data/WT_100kb/raw_\*.mat gen_part.fend counts_inter.fend

$ hifive hic-project -f 25 -n 25 -j 100000 counts_inter.fend project.fend

$ hifive hic-normalize express -f 25 -w cis project.fend

# Get and plot heatmap HiC data
$ python chr_13.py

# Get and plot compartment scores
$ python compart.py

# Get and plot violin plots
$ grep -v "-" hic_comp.bed > positive.bed

$ grep "-" hic_comp.bed > negative.bed

$ bedtools intersect -a data/WT_fpkm.bed -b positive.bed -f 0.5 -wa > positive_WT_fpkm.bed

$ bedtools intersect -a data/WT_fpkm.bed -b negative.bed -f 0.5 -wa > negative_WT_fpkm.bed

$ python violin.py

# Expression and Repression
$ python expression.py
