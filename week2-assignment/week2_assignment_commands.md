#ASSIGNMENT 2

##Step 1:
$ bwa index sacCer3.fa 
[bwa_index] Pack FASTA... 0.09 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 5.08 seconds elapse.
[bwa_index] Update BWT... 0.07 sec
[bwa_index] Pack forward-only FASTA... 0.05 sec
[bwa_index] Construct SA from BWT and Occ... 1.80 sec
[main] Version: 0.7.17-r1188
[main] CMD: bwa index sacCer3.fa
[main] Real time: 7.358 sec; CPU: 7.100 sec

##Step 2:
$ ./loop_reads_step2.sh

##Step 3:
$ ./loop_reads_step3.sh

##Step 4:
$ freebayes -f sacCer3.fa -p 1 --genotype-qualities sorted_*.bam > var.vcf


##Step 5:
$ vcffilter -f "QUAL > 20" var.vcf > var_prob_poly_gt0.99.vcf
$ head -n 1000 var_prob_poly_gt0.99.vcf > var_1000_filtered.vcf

##Step 6:
$ vcfallelicprimitives -k -g var_prob_poly_gt0.99.vcf > var_prob_poly_gt0.99_decomp.vcf 
$ head -n 1000 var_prob_poly_gt0.99_decomp.vcf > var_1000_decomposed.vcf

##Step 7:
$ snpeff download R64-1-1.86
$ snpeff ann -download R64-1-1.86 -csvStats stat_summ.txt var_prob_poly_gt0.99_decomp.vcf > var_pred_funct.vcf
$ head -n 1000 var_pred_funct.vcf > var_1000_annotated.vcf

##Step 8:
See Jupyter Notebook

