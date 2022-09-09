scripts=/home/riceUsers/xueai/soybean/SNP/script
genomefile=/home/riceUsers/xueai/soybean/genomefile/phytozome
snpfile=/home/riceUsers/xueai/soybean/SNP/genomefile

#从gene注释文件中提取所有gene的位置
python $scripts/get_gene_location.py $genomefile/Gmax_275_Wm82.a2.v1.gene.gff3 > gene_location_range.txt

#计算大豆所有SNP信息的MAF和missing
#过滤MAF>=0.01 missing<=0.2
plink --bfile $snpfile/219_snp --maf 0.01 --geno 0.2 --make-bed --out $snpfile/219_snp_filter

#根据range提取cds的SNP
plink --bfile $snpfile/219_snp_filter --extract range gene_location_range.txt --make-bed --out cds_snp/cds_rangesnp

awk '{print $NF}' gene_location_range.txt | sort | uniq > all_gene_name.txt

# for i in `cat all_gene_name.txt`
# do
	# cd single
	# awk '$5=="'$i'"{print $0}' ../gene_location_range.txt > $i.range.pos
	# # plink --threads 24 --bfile ../cds_snp/cds_rangesnp --extract range $i.range.pos --recode --out $i
	# # plink --file $i --recode --transpose --out $i
	# # plink --file $i --freq --missing --out $i
	# # rm $i.log
	# # rm $i.nosex
	# cd ../
# done

# find single/ -name "*.map" | awk -F "/" '{print $2}' | awk -F "." '{print $1"."$2}' | sort | uniq > snp_gene_name.txt

# for j in `cat snp_gene_name.txt`
# do
	# cd single
	# #获取单倍型
	# python $scripts/get_haplotype.py $j.ped > ${j}_haplotype.txt
	# #freq内容提取
	# python $scripts/get_freq.py ${j}.map ${j}.frq ${j}.lmiss > ${j}_frq_miss.txt
	# #用haplotype生成
	# python $scripts/get_ref_maf.final_soy.py $genomefile/Gmax_275_v2.0.fa ${j}_frq_miss.txt ${j}_haplotype.txt > ${j}_CDS_geno.txt
	# #或者用tped转置文件来生成
	# # python $scripts/get_ref_maf_tped.final.py $genomefile/Gmax_275_v2.0.fa ${i}_frq_miss.txt ${i}_rangesnp.tped ${i}_range.tfam> ${i}_CDS_geno.txt

	# #获取gene对应所有材料的序列(未完成)
	# # python $scripts/get_gene_3024_seq_soy.py ${j} $i.range.pos $genomefile/Gmax_275_v2.0.fa ${j}_haplotype.txt ${j}_frq_miss.txt ${j}_3024_seq.txt
	
	# cd ../
# done

for j in `cat snp_gene_name.txt`
do
	for n in $(cat year.txt)
		do 
		cd result
		cd Grain_weight
		cd ${n}
		# python $scripts/get_haplotype_phenotype.py ../../../single/${j}_haplotype.txt $snpfile/Grain_weight.txt ${n}> ${j}_GW_${n}_hap2phe.txt
		# python $scripts/get_hap2phe_anova.py ${j}_GW_${n}_hap2phe.txt > anova_${j}_${n}_GW.txt
		# python $scripts/mean_hap2phe.py ${j}_GW_${n}_hap2phe.txt Grain_weight ../../../single/${j}.map > mean_${j}_${n}_GW.txt
		python $scripts/get_material2hap.py ../../../single/${j}_haplotype.txt anova_${j}_${n}_GW.txt > ${j}_material_hap_${n}_GW.txt
        # # 合并前面两步直接由单倍型文件生成方差分析前需要的表格
        # python $scripts/get_anova_analysis_table.py ../../../single/${j}_haplotype.txt $snpfile/Grain_weight.txt ${n} > anova_${j}_${n}_GW.txt
		# # 检验数据正态分布（kstest，p>0.05）、方差齐性(levene,p>0.01)最后做差异分析
		# python $scripts/anova.py anova_${j}_${n}_GW.txt Grain_weight ${j}_${n} $snpfile/Grain_weight.txt 0.05 normal_result_${j}_${n}_GW.txt variances_result_${j}_${n}_GW.txt filter_result_${j}_${n}_GW.txt
		
		cd ../../../
	done
done

#从总的map和ped文件里依据基因注释文件将每个基因的map和ped文件生成
#先将map文件每一行后面加上序列号
# python $scripts/add_num_map.py genelocation_rangesnp.map genelocation_rangesnp_new.map 
# python $scripts/get_every_mapped.py $genomefile/Gmax_275_Wm82.a2.v1.gene.gff3 genelocation_rangesnp_new.map genelocation_rangesnp.ped

