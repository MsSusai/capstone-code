#!/usr/bin/env bash

# 单倍型分析表格
# /home/riceUsers/lhr/soybean/output/${phenotype}_old_no_normaltest/${year}/${gene}_${phenotype}_${year}_hap2phe.csv

# 多重比较结果
# /home/riceUsers/lhr/soybean/output/${phenotype}_old_no_normaltest/${year}/multiple_comparison_result_${gene}_${year}_${phenotype}.csv


for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  cd /home/riceUsers/lhr/soybean/final_results/haplotype/
  mkdir ${phenotype}
  cd ${phenotype}
  for year in 2015yzBL 2016yzBL 2017yzBL
  do
    echo "正在处理${phenotype}_${year}"
    mkdir ${year}
    cd ${year}
    for gene in $(cat /home/riceUsers/lhr/soybean/final_results/gene_loc/${phenotype}.txt)
    do
      # cp /home/riceUsers/lhr/soybean/output/${phenotype}_old_no_normaltest/${year}/${gene}_${phenotype}_${year}_hap2phe.csv .
      # cp /home/riceUsers/lhr/soybean/output/${phenotype}_old_no_normaltest/${year}/multiple_comparison_result_${gene}_${year}_${phenotype}.csv .
      cp /home/riceUsers/lhr/soybean/output/${phenotype}_old_no_normaltest/${year}/anova_result_${gene}_${year}_${phenotype}.txt .
    done
    cd ..
  done
  cd ..
done