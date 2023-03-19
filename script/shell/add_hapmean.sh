#!/usr/bin/env bash
# nohup sh final_hapdata.sh > final_hapdata.log 2>&1 &

for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  for gene in $(cat /home/riceUsers/lhr/soybean/final_results/final_loc/${phenotype}.txt)
  do
    echo "正在处理${phenotype}_${gene}"
    happath_2016=/home/riceUsers/lhr/soybean/final_results/haplotype/${phenotype}/2016yzBL/${gene}_${phenotype}_2016yzBL_hap2phe.csv
    inputpath=/home/riceUsers/lhr/soybean/final_results/database_haplotype/${phenotype}.csv
    outputpath=/home/riceUsers/lhr/soybean/final_results/hap_addmean/${phenotype}.csv
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/add_hapmean.py ${inputpath} ${happath_2016} ${gene} ${outputpath}
  done
done