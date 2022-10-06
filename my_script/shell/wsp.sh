# 水溶蛋白
# nohup sh wsp.sh > wsp.log 2>&1 &

cd /home/riceUsers/lhr/soybean/output
mkdir water_soluble_protein
cd water_soluble_protein
for year in 2015yzBL 2016yzBL 2017yzBL
do
    mkdir ${year}
    cd ${year}
    for gene in $(cat /home/riceUsers/lhr/soybean/temp_file/snp_gene_name.txt)
    do
        # 关联单倍型和表型，生成方差分析所需表格
        # 输出：${gene}_water_soluble_protein_${year}_hap2phe.csv
        echo "正在处理water_soluble_protein_${year}_${gene}"
        python /home/riceUsers/lhr/soybean/src/my_script/python_script/haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/water_soluble_protein.txt ${year} ${gene} water_soluble_protein
        # 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析(anova_lm，p<0.05)，多重比较（pairwise_tukeyhsd,p<0.05）
        python /home/riceUsers/lhr/soybean/src/my_script/python_script/anova.py /home/riceUsers/lhr/soybean/output/water_soluble_protein/${year}/${gene}_water_soluble_protein_${year}_hap2phe.csv 0.05 /home/riceUsers/lhr/soybean/output/water_soluble_protein/${year}/normality_result_${gene}_${year}_water_soluble_protein.txt /home/riceUsers/lhr/soybean/output/water_soluble_protein/${year}/variance_homogeneity_result_${gene}_${year}_water_soluble_protein.txt /home/riceUsers/lhr/soybean/output/water_soluble_protein/${year}/filter_result_${gene}_${year}_water_soluble_protein.txt /home/riceUsers/lhr/soybean/output/water_soluble_protein/${year}/anova_result_${gene}_${year}_water_soluble_protein.txt /home/riceUsers/lhr/soybean/output/water_soluble_protein/${year}/multiple_comparison_result_${gene}_${year}_water_soluble_protein.csv
    done
    cd ..
done
