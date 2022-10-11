# 含油量
# nohup sh oil.sh > oil.log 2>&1 &

cd /home/riceUsers/lhr/soybean/output
mkdir new_oil
cd new_oil

for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/new_snp_gene_name.txt)
do
    # 关联单倍型和表型，生成方差分析所需表格
    # 输出：${gene}_oil_hap2phe.csv
    echo "正在处理oil_${gene}"
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/new/new_haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/new_single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/new_snp_files/trait/oil.txt ${gene} oil
    # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/new/new_anova.py /home/riceUsers/lhr/soybean/output/new_oil/${gene}_oil_hap2phe.csv 0.05 /home/riceUsers/lhr/soybean/output/new_oil/normality_result_${gene}_oil.txt /home/riceUsers/lhr/soybean/output/new_oil/variance_homogeneity_result_${gene}_oil.txt /home/riceUsers/lhr/soybean/output/new_oil/filter_result_${gene}_oil.txt /home/riceUsers/lhr/soybean/output/new_oil/anova_result_${gene}_oil.txt /home/riceUsers/lhr/soybean/output/new_oil/multiple_comparison_result_${gene}_oil.csv
done