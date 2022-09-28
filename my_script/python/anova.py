# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/27  16:42 
# 名称：anova.PY
# 工具：PyCharm
# 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析（F），多重比较（p<0.05）

# 运行：
# windows：python .\my_script\python\anova.py .\sample_file\Glyma.20G250200_protein_2015yzBL_hap2phe.csv .\sample_file\Pro_content.txt Pro_content 2015yzBL Glyma.20G250200 0.05 normal_result_Glyma.20G250200_2015_Oil.txt variances_result_Glyma.20G250200_2015_Pro.txt filter_result_Glyma.20G250200_2015_Pro.txt


import sys
import pathlib
from typing import Union

import pandas as pd
import numpy as np

from scipy.stats import kstest
from scipy.stats import levene
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def anova_filter(haplotype_df: pd.DataFrame, parameter: str) -> pd.DataFrame:
	"""
	过滤样本单倍型
	单倍型包含数据数目>总材料数目*parameter
	"""
	# 保留不少于规定数目的单倍型（219*0.05=10.9）
	df_filter = pd.Series(haplotype_df["type"].value_counts() >= len(haplotype_df) * float(parameter))
	for hap, values in df_filter.items():
		if not values:
			# 将少于10.9个样本的单倍型从表中剔除
			haplotype_df = haplotype_df[~haplotype_df["type"].isin([hap])]
	return haplotype_df


def normality_test(filtered_haplotype_df: pd.DataFrame):
	"""
	正态分布检验
	使用 K-S test
	"""
	hap_series = pd.Series(filtered_haplotype_df["type"].value_counts())
	for hap in hap_series.keys():
		hap_df = filtered_haplotype_df[filtered_haplotype_df["type"] == hap]
		mean = hap_df["value"].mean()
		std = hap_df["value"].std()
		print(kstest(hap_df["value"], 'norm', (mean, std))) # p>0.05符合正态分布
		


def main():
	# 输入文件与参数
	haplotype_df: pd.DataFrame = pd.read_csv(sys.argv[1], index_col=0)  # 单倍型数据
	phenotype_path: Union[str, pathlib.Path] = sys.argv[2]  # 表型数据
	phenotype: str = sys.argv[3]  # 表型
	year_flag: str = sys.argv[4]  # 年份
	gene_accession: str = sys.argv[5]  # 基因号
	parameter: str = sys.argv[6]  # 规定的参数，作用是:样本总数目*parameter=保留不少于规定数目的单倍型
	
	# 输出文件
	kstest_path: [str, pathlib.Path] = sys.argv[7]  # 正态分布检验文件路径
	levene_path: [str, pathlib.Path] = sys.argv[8]  # 方差齐性检验文件路径
	filter_path: [str, pathlib.Path] = sys.argv[9]  # 过滤文件路径
	filter_list: list = []  # 过滤文件检验结果
	
	filtered_haplotype_df = anova_filter(haplotype_df, parameter)  # 过滤满足条件的单倍型
	# print("There are "
	#       + str(len(haplotype_df["type"].value_counts()) - len(filtered_haplotype_df["type"].value_counts())) +
	#       " haplotypes that contain less than 5 materials and are filtered, and the remaining "
	#       + str(len(filtered_haplotype_df["type"].value_counts())) +
	#       " haplotypes are used for subsequent analysis.")
	# # 输出过滤文件检验结果
	# filter_list.append("all haplotype: " + str(len(haplotype_df["type"].value_counts())) + "\n")
	# filter_list.append("filtered haplotype: " + str(
	# 	len(haplotype_df["type"].value_counts()) - len(filtered_haplotype_df["type"].value_counts())) + "\n")
	# filter_list.append("remain haplotype " + str(len(filtered_haplotype_df["type"].value_counts())) + "\n")
	# with open(filter_path, "w") as filter_file:
	# 	filter_file.writelines(filter_list)
	
	normality_test(filtered_haplotype_df)


if __name__ == '__main__':
	main()
