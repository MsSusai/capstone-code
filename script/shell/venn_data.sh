#!/usr/bin/env bash
# nohup sh final_hapdata.sh > final_hapdata.log 2>&1 &
# multiple_comparison_result_${gene}_${year}_${phenotype}.csv

for phenotype in $(cat /home/riceUsers/lhr/soybean/genomefile/phenotype.txt)
do
  cd /home/riceUsers/lhr/soybean/output/${phenotype}_old_no_normaltest/
  for year in 2015yzBL 2016yzBL 2017yzBL
  do
    cd ${year}
    echo "正在处理${phenotype}_${year}"
    ls|grep "multiple_comparison_result" > ${year}_${phenotype}.txt
    for filename in $(cat ${year}_${phenotype}.txt)
      do
        echo "${filename: 27: 15}" >> /home/riceUsers/lhr/soybean/final_results/output/${year}_${phenotype}.txt
      done
    cd ..
  done
  cd ..
done