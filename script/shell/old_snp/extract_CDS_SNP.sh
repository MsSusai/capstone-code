#!/usr/bin/env bash

# 计算大豆所有SNP信息的MAF和missing，对缺失数据进行筛选
# 设置过滤条件 MAF>=0.01 missing<=0.2

# nohup sh extract_CDS_SNP.sh > extract_CDS_SNP.log 2>&1 &

# 输入SNP文件
# /home/riceUsers/lhr/soybean/genomefile/219_snp/219_snp
# 输出过滤文件
# /home/riceUsers/lhr/soybean/temp_file/219_snp_filterdir/219_snp_filter

# plink --bfile /home/riceUsers/lhr/soybean/genomefile/219_snp/219_snp --maf 0.01 --geno 0.2 --make-bed --out /home/riceUsers/lhr/soybean/temp_file/219_snp_filterdir/219_snp_filter

# 根据range提取cds的SNP
# plink --bfile /home/riceUsers/lhr/soybean/temp_file/219_snp_filterdir/219_snp_filter --extract range /home/riceUsers/lhr/soybean/temp_file/gene_location.txt --make-bed --out /home/riceUsers/lhr/soybean/temp_file/cds_snp/cds_rangesnp

# 对提取的cds区域内的基因名称去重
# awk '{print $NF}' /home/riceUsers/lhr/soybean/temp_file/gene_location.txt | sort | uniq > /home/riceUsers/lhr/soybean/temp_file/all_gene_name.txt

# 有SNP的基因名称获取
for i in $(cat /home/riceUsers/lhr/soybean/temp_file/all_gene_name.txt)
do
	cd /home/riceUsers/lhr/soybean/temp_file/single
	awk '$5=="'$i'"{print $0}' /home/riceUsers/lhr/soybean/temp_file/gene_location.txt > $i.range.pos
	plink --threads 24 --bfile /home/riceUsers/lhr/soybean/temp_file/cds_snp/cds_rangesnp --extract range $i.range.pos --recode --out $i
	plink --file $i --recode --transpose --out $i
	plink --file $i --freq --missing --out $i
	rm $i.log
	rm $i.nosex
	cd ../
done

find single/ -name "*.map" | awk -F "/" '{print $2}' | awk -F "." '{print $1"."$2}' | sort | uniq > /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt


