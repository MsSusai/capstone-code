scripts=/home/riceUsers/xueai/soybean/SNP/script
genomefile=/home/riceUsers/xueai/soybean/genomefile/phytozome
snpfile=/home/riceUsers/xueai/soybean/SNP/genomefile


for j in `cat snp_gene_name.txt`
do
	for n in 2015 2016 2017
		do 
		cd result
		cd Oil_content
		cd ${n}
		# python $scripts/get_haplotype_phenotype.py ../../../single/${j}_haplotype.txt $snpfile/Oil_content.txt ${n}> ${j}_Oil_${n}_hap2phe.txt
		# python $scripts/get_hap2phe_anova.py ${j}_Oil_${n}_hap2phe.txt > anova_${j}_${n}_Oil.txt
		# python $scripts/mean_hap2phe.py ${j}_Oil_${n}_hap2phe.txt Oil_content ../../../single/${j}.map > mean_${j}_${n}_Oil.txt
		python $scripts/get_material2hap.py ../../../single/${j}_haplotype.txt anova_${j}_${n}_Oil.txt > ${j}_material_hap_${n}_Oil.txt
        # # 合并前面两步直接由单倍型文件生成方差分析前需要的表格
        # python $scripts/get_anova_analysis_table.py ../../../single/${j}_haplotype.txt $snpfile/Oil_content.txt ${n} > anova_${j}_${n}_Oil.txt
		# # 检验数据正态分布（kstest，p>0.05）、方差齐性(levene,p>0.01)最后做差异分析
		# python $scripts/anova.py anova_${j}_${n}_Oil.txt Oil_content ${j}_${n} $snpfile/Oil_content.txt 0.05 normal_result_${j}_${n}_Oil.txt variances_result_${j}_${n}_Oil.txt filter_result_${j}_${n}_Oil.txt
		
		cd ../../../
	done
done