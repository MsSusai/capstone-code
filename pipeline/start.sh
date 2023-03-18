#!/usr/bin/env bash

#----------------------------------------------------------------------------------------------
# 从gene注释文件中提取所有gene的位置

# 注释文件
# /home/riceUsers/lhr/soybean/genomefile/Gmax_275_Wm82.a2.v1.gene.gff3

python /home/riceUsers/lhr/soybean/src/my_script/python_script/extract_location.py > /home/riceUsers/lhr/soybean/temp_file/gene_location.txt

#----------------------------------------------------------------------------------------------

# 计算大豆所有SNP信息的MAF和missing，对缺失数据进行筛选
# 设置过滤条件 MAF>=0.01 missing<=0.2

# 输入SNP文件
# /home/riceUsers/lhr/soybean/genomefile/219_snp/219_snp
# 输出过滤文件
# /home/riceUsers/lhr/soybean/temp_file/219_snp_filterdir/219_snp_filter

plink --bfile /home/riceUsers/lhr/soybean/genomefile/219_snp/219_snp --maf 0.01 --geno 0.2 --make-bed --out /home/riceUsers/lhr/soybean/temp_file/219_snp_filterdir/219_snp_filter

# 根据range提取cds的SNP
plink --bfile /home/riceUsers/lhr/soybean/temp_file/219_snp_filterdir/219_snp_filter --extract range /home/riceUsers/lhr/soybean/temp_file/gene_location.txt --make-bed --out /home/riceUsers/lhr/soybean/temp_file/cds_snp/cds_rangesnp

# 对提取的cds区域内的基因名称去重
awk '{print $NF}' /home/riceUsers/lhr/soybean/temp_file/gene_location.txt | sort | uniq > /home/riceUsers/lhr/soybean/temp_file/all_gene_name.txt

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

#----------------------------------------------------------------------------------------------

# 获取每个基因的单倍型
for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt)
do
  python /home/riceUsers/lhr/soybean/src/my_script/python_script/get_haplotype.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}.ped > /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt
done

#----------------------------------------------------------------------------------------------
# 进行单倍型与表型关联分析

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
      echo "正在处理${phenotype}_${year}_${gene}"
      python /home/riceUsers/lhr/soybean/src/my_script/python_script/hap2phe.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/${phenotype}.txt ${year} ${gene} ${phenotype}
      # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
      python /home/riceUsers/lhr/soybean/src/my_script/python_script/anova.py /home/riceUsers/lhr/soybean/output/${phenotype}/${year}/${gene}_${phenotype}_${year}_hap2phe.csv 0.05 /home/riceUsers/lhr/soybean/output/${phenotype}/${year}/normality_result_${gene}_${year}_${phenotype}.txt /home/riceUsers/lhr/soybean/output/${phenotype}/${year}/variance_homogeneity_result_${gene}_${year}_${phenotype}.txt /home/riceUsers/lhr/soybean/output/${phenotype}/${year}/filter_result_${gene}_${year}_${phenotype}.txt /home/riceUsers/lhr/soybean/output/${phenotype}/${year}/anova_result_${gene}_${year}_${phenotype}.txt /home/riceUsers/lhr/soybean/output/${phenotype}/${year}/multiple_comparison_result_${gene}_${year}_${phenotype}.csv
    done
    cd ..
  done
  cd ..
done
