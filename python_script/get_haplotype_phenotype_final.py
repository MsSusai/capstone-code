#python $scripts/get_haplotype_phenotype_final.py GW_2013_hap2phe.txt > GW_2013_hap2phe_final.txt

import sys

print ("material\thaplotype\tphenotype")
for line in open(sys.argv[1],"r"):
    l = line.strip().split("\t")
    l[1] = l[1].replace('-','N').replace('M','N').replace('S','N').replace('K','N').replace('R','N').replace('W','N').replace('Y','N')
    print ("\t".join(l))