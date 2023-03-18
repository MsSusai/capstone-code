#! /usr/bin/env bash

# nohup sh extract_snp.sh > extract_snp.log 2>&1 &

# 有SNP的基因获取
for i in $(cat /home/riceUsers/xueai/soybean/SNP/all_gene_name.txt)
do
	cd /home/riceUsers/lhr/soybean/temp_file/new_single
	awk '$5=="'${i}'"{print $0}' /home/riceUsers/xueai/soybean/SNP/gene_location_range.txt > ${i}.range.pos
	plink --threads 24 --bfile /home/riceUsers/lhr/soybean/genomefile/new_snp_files/cds_rangesnp_new --extract range ${i}.range.pos --recode --out ${i}
	plink --file ${i} --recode --transpose --out ${i}
	plink --file ${i} --freq --missing --out ${i}
	rm ${i}.log
	rm ${i}.nosex
	cd ../
done

find new_single/ -name "*.map" | awk -F "/" '{print $2}' | awk -F "." '{print $1"."$2}' | sort | uniq > /home/riceUsers/lhr/soybean/temp_file/new_snp_gene_name.txt
