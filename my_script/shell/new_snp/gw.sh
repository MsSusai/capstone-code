# 粒重
# nohup sh gw.sh > gw.log 2>&1 &

cd /home/riceUsers/lhr/soybean/output
mkdir new_grain_weight
cd new_grain_weight

for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/new_snp_gene_name.txt)
do
    # 关联单倍型和表型，生成方差分析所需表格
    # 输出：${gene}_grain_weight_hap2phe.csv
    echo "正在处理grain_weight_${gene}"
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/new/new_haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/new_single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/new_snp_files/trait/grain_weight.txt ${gene} grain_weight
    # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/new/new_anova.py /home/riceUsers/lhr/soybean/output/new_grain_weight/${gene}_grain_weight_hap2phe.csv 0.05 /home/riceUsers/lhr/soybean/output/new_grain_weight/normality_result_${gene}_grain_weight.txt /home/riceUsers/lhr/soybean/output/new_grain_weight/variance_homogeneity_result_${gene}_grain_weight.txt /home/riceUsers/lhr/soybean/output/new_grain_weight/filter_result_${gene}_grain_weight.txt /home/riceUsers/lhr/soybean/output/new_grain_weight/anova_result_${gene}_grain_weight.txt /home/riceUsers/lhr/soybean/output/new_grain_weight/multiple_comparison_result_${gene}_grain_weight.csv
done
