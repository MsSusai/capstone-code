# 粒重
# nohup sh gw.sh > gw.log 2>&1 &

cd /home/riceUsers/lhr/soybean/output
mkdir grain_weight
cd grain_weight
for year in 2015yzBL 2016yzBL 2017yzBL
do
    mkdir ${year}
    cd ${year}
    for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt)
    do
        # 关联单倍型和表型，生成方差分析所需表格
        # 输出：${gene}_grain_weight_${year}_hap2phe.csv
        echo "正在处理grain_weight_${year}_${gene}"
        python /home/riceUsers/lhr/soybean/src/my_script/python_script/haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/grain_weight.txt ${year} ${gene} grain_weight
        # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
        python /home/riceUsers/lhr/soybean/src/my_script/python_script/anova.py /home/riceUsers/lhr/soybean/output/grain_weight/${year}/${gene}_grain_weight_${year}_hap2phe.csv 0.05 /home/riceUsers/lhr/soybean/output/grain_weight/${year}/normality_result_${gene}_${year}_grain_weight.txt /home/riceUsers/lhr/soybean/output/grain_weight/${year}/variance_homogeneity_result_${gene}_${year}_grain_weight.txt /home/riceUsers/lhr/soybean/output/grain_weight/${year}/filter_result_${gene}_${year}_grain_weight.txt /home/riceUsers/lhr/soybean/output/grain_weight/${year}/anova_result_${gene}_${year}_grain_weight.txt /home/riceUsers/lhr/soybean/output/grain_weight/${year}/multiple_comparison_result_${gene}_${year}_grain_weight.csv
    done
    cd ..
done
cd ..