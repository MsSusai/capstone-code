source /home/riceUsers/fzr/repo/src/basic_func/func_parallel.sh
sparallel 30

scripts=/home/riceUsers/xueai/soybean/SNP/script
snpfile=/home/riceUsers/xueai/soybean/SNP/genomefile

for j in `cat snp_gene_name.txt`
do
	
    read -u3
    {	
	
		for n in $(cat year.txt)
			do 
				cd result
				cd Grain_weight
				cd ${n}
				rm anova_table_Grain_weight_${j}_${n}.txt anova_result_Grain_weight_${j}_${n}.txt normal_result_${j}_${n}_GW.txt variances_result_${j}_${n}_GW.txt filter_result_${j}_${n}_GW.txt
				python $scripts/anova.py anova_${j}_${n}_GW.txt Grain_weight ${j}_${n} $snpfile/Grain_weight.txt 0.05 normal_result_${j}_${n}_GW.txt variances_result_${j}_${n}_GW.txt filter_result_${j}_${n}_GW.txt
		
				cd ../../../
			done
        echo >&3
    }&
done
wait

eparallel