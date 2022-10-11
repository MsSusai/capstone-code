# 花期
# nohup sh flower_day_no_normaltest.sh > flower_day_no_normaltest.log 2>&1 &

cd /home/riceUsers/lhr/soybean/output
mkdir flower_day_no_normaltest
cd flower_day_no_normaltest

for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/new_snp_gene_name.txt)
do
    # 关联单倍型和表型，生成方差分析所需表格
    # 输出：${gene}_flower_day_hap2phe.csv
    echo "正在处理flower_day_${gene}"
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/new/new_haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/new_single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/new_snp_files/trait/flower_day.txt ${gene} flower_day
    # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
    python /home/riceUsers/lhr/soybean/src/my_script/python_script/new/new_anova_no_normaltest.py /home/riceUsers/lhr/soybean/output/flower_day_no_normaltest/${gene}_flower_day_hap2phe.csv 0.05 /home/riceUsers/lhr/soybean/output/flower_day_no_normaltest/normality_result_${gene}_flower_day.txt /home/riceUsers/lhr/soybean/output/flower_day_no_normaltest/variance_homogeneity_result_${gene}_flower_day.txt /home/riceUsers/lhr/soybean/output/flower_day_no_normaltest/filter_result_${gene}_flower_day.txt /home/riceUsers/lhr/soybean/output/flower_day_no_normaltest/anova_result_${gene}_flower_day.txt /home/riceUsers/lhr/soybean/output/flower_day_no_normaltest/multiple_comparison_result_${gene}_flower_day.csv
done
