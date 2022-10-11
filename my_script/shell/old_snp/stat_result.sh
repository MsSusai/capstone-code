#!/usr/bin/env bash

# 统计方差分析运行结果


for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  cd /home/riceUsers/lhr/soybean/output
  cd ${phenotype}_old_no_normaltest
  for year in 2015yzBL 2016yzBL 2017yzBL
  do
    cd ${year}
    echo "正在运行${phenotype}_${year}"
    echo -e "${phenotype}_${year}: \n `ls | grep "normality_result"`" > /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_normality_result.txt
    sed  -i "1i\ $(cat /home/riceUsers/lhr/soybean/output/result/${phenotype}_${year}_normality_result.txt | wc -l)" /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_normality_result.txt
    echo -e "${phenotype}_${year}: \n `ls | grep "variance_homogeneity_result"`" > /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_variance_homogeneity_result.txt
    sed  -i "1i\ $(cat /home/riceUsers/lhr/soybean/output/result/${phenotype}_${year}_variance_homogeneity_result.txt | wc -l)" /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_variance_homogeneity_result.txt
    echo -e "${phenotype}_${year}: \n `ls | grep "anova_result"`" > /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_anova_result.txt
    sed  -i "1i\ $(cat /home/riceUsers/lhr/soybean/output/result/${phenotype}_${year}_anova_result.txt | wc -l)" /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_anova_result.txt
    echo -e "${phenotype}_${year}: \n `ls | grep "multiple_comparison"`" > /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_multiple_comparison.txt
    sed  -i "1i\ $(cat /home/riceUsers/lhr/soybean/output/result/${phenotype}_${year}_multiple_comparison.txt | wc -l)" /home/riceUsers/lhr/soybean/output/result/${phenotype}_old_no_normaltest_${year}_multiple_comparison.txt
    cd ..
  done
  cd ..
done