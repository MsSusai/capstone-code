#!/usr/bin/env bash

# 进行单倍型与表型关联分析
# nohup sh haplotype_analysis.sh > haplotype_analysis.log 2>&1 &

# 单倍型文件
# /home/riceUsers/lhr/soybean/temp_file/single/${}_haplotype.txt

# 表型文件
# /home/riceUsers/lhr/soybean/genomefile/oil_content.txt protein_content.txt grain_weight.txt water_soluble_protein_content.txt

# cds区域有snp的基因名称文件
# /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt

# 年份
# 2015yzBL 2016yzBL 2017yzBL

# 表型
# /home/riceUsers/lhr/soybean/genomefile/phenotype.txt

for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  cd /home/riceUsers/lhr/soybean/output
  mkdir ${phenotype}
  cd ${phenotype}
  for year in 2015yzBL 2016yzBL 2017yzBL
  do
    mkdir ${year}
    cd ${year}
    for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt)
    do
      # 关联单倍型和表型，生成方差分析所需表格
      # 输出：${gene}_${phenotype}_${year}_hap2phe.csv
      python /home/riceUsers/lhr/soybean/src/my_script/python_script/haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/${phenotype}.txt ${year} ${gene} ${phenotype}
      # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
#      python /home/riceUsers/lhr/soybean/src/my_script/python_script/anova.py
    done
    cd ..
  done
  cd ..
done







