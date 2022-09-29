# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/27  16:42 
# 名称：anova.PY
# 工具：PyCharm
# 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析（F），多重比较（p<0.05）

# 运行：
# windows: python .\my_script\python\anova.py .\sample_file\Glyma.20G250200_protein_2015yzBL_hap2phe.csv Pro_content 2015yzBL Glyma.20G250200 0.05 normal_result_Glyma.20G250200_2015_Oil.txt variances_result_Glyma.20G250200_2015_Pro.txt filter_result_Glyma.20G250200_2015_Pro.txt
# linux: python

import sys
import pathlib
from typing import Union

import pandas as pd

from scipy.stats import shapiro
from scipy.stats import levene
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def anova_filter(haplotype_df: pd.DataFrame, parameter: str) -> pd.DataFrame:
	"""
	过滤样本单倍型
	标准：单倍型包含数据数目>总材料数目*parameter
	"""
	# 保留不少于规定数目的单倍型（219*0.05=10.9）
	df_filter = pd.Series(haplotype_df["type"].value_counts() >= len(haplotype_df) * float(parameter))
	for hap, values in df_filter.items():
		if not values:
			# 将少于10.9个样本的单倍型从表中剔除
			haplotype_df = haplotype_df[~haplotype_df["type"].isin([hap])]
	return haplotype_df


def normality_test(filtered_haplotype_df: pd.DataFrame) -> list:
	"""
	正态分布检验
	使用 S-W test
	p<0.05时说明数据不符合正态分布
	"""
	result: list = []
	flag: bool = True
	hap_series = pd.Series(filtered_haplotype_df["type"].value_counts())
	
	for hap in hap_series.keys():
		hap_df = filtered_haplotype_df[filtered_haplotype_df["type"] == hap]
		stat, p_value = shapiro(hap_df["value"])
		if p_value < 0.05:  # 不满足正态分布
			flag = False
		result.append([hap, stat, p_value])  # p>0.05符合正态分布
	result.append(flag)  # 数据是否满足正态分布
	return result


def variance_homogeneity_test(filtered_haplotype_df: pd.DataFrame) -> list:
	"""
	方差齐性检验
	使用 levene test
	p<0.01时说明数据不具有方差齐性
	"""
	data_list: list = []
	flag: bool = True
	hap_series = pd.Series(filtered_haplotype_df["type"].value_counts())
	
	for hap in hap_series.keys():
		hap_df = filtered_haplotype_df[filtered_haplotype_df["type"] == hap]
		data_list.append(hap_df["value"].values)
	stat, p_value = levene(*data_list)
	if p_value < 0.01:  # 不具有方差齐性
		flag = False
	return [stat, p_value, flag]


def anova_analysis(filtered_haplotype_df: pd.DataFrame):
	model = ols('value~C(type)', data=filtered_haplotype_df).fit()
	anova_table = anova_lm(model, typ=2)
	p_value = anova_table.loc['C(type)', 'PR(>F)']
	f_value = anova_table.loc['C(type)', 'F']


def multiple_comparison():
	pass


def main():
	# 输入文件与参数
	haplotype_df: pd.DataFrame = pd.read_csv(sys.argv[1], index_col=0)  # 单倍型-表型数据
	phenotype: str = sys.argv[2]  # 表型
	year_flag: str = sys.argv[3]  # 年份
	gene_accession: str = sys.argv[4]  # 基因号
	parameter: str = sys.argv[5]  # 规定的参数，作用是:样本总数目*parameter=保留不少于规定数目的单倍型
	
	# 输出文件
	swtest_path: Union[str, pathlib.Path] = sys.argv[6]  # 正态分布检验文件路径
	levene_path: Union[str, pathlib.Path] = sys.argv[7]  # 方差齐性检验文件路径
	filter_path: Union[str, pathlib.Path] = sys.argv[8]  # 过滤文件路径
	filter_list: list = []  # 过滤文件检验结果
	
	filtered_haplotype_df = anova_filter(haplotype_df, parameter)  # 过滤满足条件的单倍型-表型
	print("There are "
	      + str(len(haplotype_df["type"].value_counts()) - len(filtered_haplotype_df["type"].value_counts())) +
	      " haplotypes that contain less than 5 materials and are filtered, and the remaining "
	      + str(len(filtered_haplotype_df["type"].value_counts())) +
	      " haplotypes are used for subsequent analysis.")
	# 输出过滤文件检验结果
	filter_list.append("all haplotype: " + str(len(haplotype_df["type"].value_counts())) + "\n")
	filter_list.append("filtered haplotype: " + str(
		len(haplotype_df["type"].value_counts()) - len(filtered_haplotype_df["type"].value_counts())) + "\n")
	filter_list.append("remain haplotype: " + str(len(filtered_haplotype_df["type"].value_counts())) + "\n")
	with open(filter_path, "w") as filter_file:
		filter_file.writelines(filter_list)
	
	if len(filtered_haplotype_df["type"].value_counts()) > 1:  # 检测过滤后满足条件的单倍型-表型组数，不足一组的无法进行方差分析
		swtest_result: list = normality_test(filtered_haplotype_df)  # 进行正态性检验
		# 输出正态分布检验结果
		with open(swtest_path, "w") as swtest_file:
			for line in swtest_result:
				if line is not True or False:
					swtest_file.writelines(f"haplotype: {line[0]}\n"
					                       f"statistic: {line[1]}\n"
					                       f"pvalue: {line[2]}\n" + "\n")
				else:
					swtest_file.writelines(f"result: {line}\n")
		
		if True in swtest_result:  # 单倍型-表型数据满足正态分布
			levene_result: list = variance_homogeneity_test(filtered_haplotype_df)  # 进行方差齐性检验
			# 输出方差齐性检验结果
			with open(levene_path, "w") as levene_file:
				levene_file.writelines(f"statistic: {levene_result[0]}\n"
				                       f"pvalue: {levene_result[1]}\n"
				                       f"variance_homogeneity: {levene_result[2]}\n")
			
			if levene_result[2] is True:  # 数据满足方差齐性
				anova_analysis(filtered_haplotype_df)  # 进行方差分析
			
			
			else:  # 数据不满足方差齐性
				print("There is no difference in the average phenotype of the two haplotypes")
		
		
		else:  # 单倍型-表型数据不满足正态分布
			print("The data is not completely in accordance with the normal distribution")
			with open(levene_path, "w") as levene_file:
				levene_file.write("The data is not completely in accordance with the normal distribution")
	
	else:  # 单倍型-表型数据只有一组或更少，无法进行方差分析
		print("There is only 1 group of haplotype or less, so the gene could not perform analysis of variance")
		with open(swtest_path, "w") as swtest_file:
			swtest_file.write(
				"There is only 1 group of haplotype or less, so the gene could not perform analysis of variance")


if __name__ == '__main__':
	main()
