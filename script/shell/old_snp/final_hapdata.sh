#!/usr/bin/env bash
# nohup sh final_hapdata.sh > final_hapdata.log 2>&1 &

for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  for gene in $(cat /home/riceUsers/lhr/soybean/final_results/gene_loc/${phenotype}.txt)
  do
    echo "正在处理${phenotype}_${gene}"
    happath_2015=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2015yzBL/${gene}_${phenotype}_2015yzBL_hap2phe.csv
    happath_2016=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2016yzBL/${gene}_${phenotype}_2016yzBL_hap2phe.csv
    happath_2017=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2017yzBL/${gene}_${phenotype}_2017yzBL_hap2phe.csv
    multpath_2015=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2015yzBL/multiple_comparison_result_${gene}_2015yzBL_${phenotype}.csv
    multpath_2016=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2016yzBL/multiple_comparison_result_${gene}_2016yzBL_${phenotype}.csv
    multpath_2017=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2017yzBL/multiple_comparison_result_${gene}_2017yzBL_${phenotype}.csv
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/old/hapdata_for_database.py ${happath_2015} ${happath_2016} ${happath_2017} ${multpath_2015} ${multpath_2016} ${multpath_2017} ${gene} ${phenotype} /home/riceUsers/lhr/soybean/final_results/output/${phenotype}.csv
  done
done