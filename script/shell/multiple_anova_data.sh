#!/usr/bin/env bash
# nohup sh multiple_anova_data.sh > multiple_anova_data.log 2>&1 &

for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  for gene in $(cat /home/riceUsers/lhr/soybean/final_results/gene_loc/${phenotype}.txt)
  do
    echo "正在处理${phenotype}_${gene}"
    multpath_2015=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2015yzBL/multiple_comparison_result_${gene}_2015yzBL_${phenotype}.csv
    multpath_2016=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2016yzBL/multiple_comparison_result_${gene}_2016yzBL_${phenotype}.csv
    multpath_2017=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2017yzBL/multiple_comparison_result_${gene}_2017yzBL_${phenotype}.csv
    anovapath_2017=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2017yzBL/anova_result_${gene}_2017yzBL_${phenotype}.txt
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/multiple_data.py ${multpath_2015} ${multpath_2016} ${multpath_2017} ${gene} ${phenotype} /home/riceUsers/lhr/soybean/final_results/output/multiple_data_${phenotype}.csv
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/anova_data.py ${anovapath_2017} ${gene} ${phenotype} /home/riceUsers/lhr/soybean/final_results/output/anova_data_${phenotype}.csv
  done
done