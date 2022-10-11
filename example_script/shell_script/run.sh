####处理数据

####   SNP_genotype


####    已经过滤好了
plink --noweb --allow-extra-chr --bfile QC --geno 0.1 --maf 0.02 --make-bed --out QC --threads 6
#--allow-extra-chr 允许其他染色体，比如scaffold
#--noweb 不连接网络

#### 将带*号的SNP删除
grep "*" QC.bim  | awk '{print $2}' > rm_ID.txt
plink --bfile QC --allow-extra-chr --exclude rm_ID.txt --make-bed --out QC_filter
#### 将SNP和indel分开
plink --bfile QC_filter --snps-only --make-bed --out onlysnp
plink --bfile onlysnp --recode --out onlysnp
awk -F "\t" '{print $1"\t"$4"\t"$4"\t"$2}' onlysnp.map > onlysnp.range
plink --bfile QC_filter --exclude range onlysnp.range --make-bed --out onlyindel
plink --bfile onlyindel --recode --out onlyindel

####  利用LD信息来删减SNP
plink --bfile onlysnp --indep-pairwise 50 10 0.2 --out snp_filterLD
plink --bfile onlysnp  --extract snp_filterLD.prune.in --make-bed --out snp_filterLD
plink --bfile snp_filterLD --recode --out snp_filterLD

#### 提取cds上的snp
# 从gene注释文件中提取所有gene的位置（已完成）
#python $scripts/get_gene_location.py $genomefile/Gmax_275_Wm82.a2.v1.gene.gff3 > /home/riceUsers/xueai/soybean/SNP/gene_location_range.txt
# 根据range提取cds的SNP
plink --bfile onlysnp --extract range /home/riceUsers/xueai/soybean/SNP/gene_location_range.txt --make-bed --out cds_rangesnp_new
plink --bfile cds_rangesnp_new --recode --out cds_rangesnp_new 
#将map文件按照染色体分开
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
	awk '$1=="'${i}'"{print $0}'  SNP_genotype/cds_rangesnp_new.map > SNP_genotype/cds_chrsplit/cds_rangesnp_new_${i}.map
done

###基于cds删除LD
plink --bfile cds_rangesnp_new --indep-pairwise 50 10 0.2 --out cds_snp_filterLD
plink --bfile onlysnp  --extract cds_snp_filterLD.prune.in --make-bed --out cds_snp_filterLD
plink --bfile cds_snp_filterLD --recode --out cds_snp_filterLD

#### gene_expression
###将表达矩阵计算为表达能力矩阵
###某个基因的表达能力指该基因在某个特定样本中的表达相对于其他基因而言的表达能力，所以对于表达矩阵来说，要一列一列的计算
###因此有三种办法：

###1.利用awk转置该表达矩阵
awk 'BEGIN{FS=OFS="\t"}{for(i=1;i<NF+1;i++){a[NR,i]=$i}}END{for(i=1;i<NF+1;i++){for(j=1;j<NR;j++){printf a[j,i]"\t"}print a[j,i]}}' gene_expression/leaf_21pm_gene.txt > gene_expression/leaf_21pm_gene_trans.txt

###2.用for循环嵌套循环该矩阵
python scripts/expression_capacities_matrix.py gene_expression/leaf_21pm_gene.txt gene_expression/leaf_21pm_gene_EC.txt
python scripts/ncRNA_ECP.py gene_expression/leaf_21pm_gene_EC.txt > gene_expression/leaf_21pm_gene_final.txt

##3.用pandas将矩阵看作是excel格式直接处理列


