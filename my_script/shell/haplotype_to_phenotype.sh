#!/usr/bin/env bash

# nohup sh haplotype_to_phenotype.sh > haplotype_to_phenotype.log 2>&1 &

# 获取每个基因的单倍型
for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt)
do
  python /home/riceUsers/lhr/soybean/src/my_script/python_script/haplotype.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}.ped > /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt
done