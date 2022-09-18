scripts=/home/riceUsers/xueai/soybean/SNP/script
genomefile=/home/riceUsers/xueai/soybean/genomefile/phytozome
snpfile=/home/riceUsers/xueai/soybean/SNP/genomefile


for j in `cat snp_gene_name.txt`
do
	for n in 2015 2016 2017
		do 
		cd result
		cd Wsp_content
		cd ${n}
		# python $scripts/get_haplotype_phenotype.py ../../../single/${j}_haplotype.txt $snpfile/Wsp_content.txt ${n}> ${j}_Wsp_${n}_hap2phe.txt
		# python $scripts/get_hap2phe_anova.py ${j}_Wsp_${n}_hap2phe.txt > anova_${j}_${n}_Wsp.txt
		# python $scripts/mean_hap2phe.py ${j}_Wsp_${n}_hap2phe.txt Wsp_content ../../../single/${j}.map > mean_${j}_${n}_Wsp.txt
		python $scripts/get_material2hap.py ../../../single/${j}_haplotype.txt anova_${j}_${n}_Wsp.txt > ${j}_material_hap_${n}_Wsp.txt
        # # 合并前面两步直接由单倍型文件生成方差分析前需要的表格
        # python $scripts/get_anova_analysis_table.py ../../../single/${j}_haplotype.txt $snpfile/Wsp_content.txt ${n} > anova_${j}_${n}_Wsp.txt
		# # 检验数据正态分布（kstest，p>0.05）、方差齐性(levene,p>0.01)最后做差异分析
		# python $scripts/anova.py anova_${j}_${n}_Wsp.txt Wsp_content ${j}_${n} $snpfile/Wsp_content.txt 0.05 normal_result_${j}_${n}_Wsp.txt variances_result_${j}_${n}_Wsp.txt filter_result_${j}_${n}_Wsp.txt
		
		cd ../../../
	done
done