# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/27  16:42 
# 名称：anova.PY
# 工具：PyCharm
# 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析（F），多重比较（p<0.05）

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


def anova_filter(haplotype_df: pd.DataFrame):
	pass


def main():
	# 输入文件与参数
	haplotype_df: pd.DataFrame = pd.read_csv(sys.argv[1], header=0, index_col=None)  # 单倍型数据
	phenotype_file: Union[str, pathlib.Path] = sys.argv[2]  # 表型数据
	phenotype: str = sys.argv[3]  # 表型
	year_flag: str = sys.argv[4]  # 年份
	gene_accession: str = sys.argv[5]  # 基因号
	p_value: str = sys.argv[6]  # p值
	
	# 输出文件
	kstest_file: [str, pathlib.Path] = sys.argv[7]  # 正态分布检验结果
	levene_file: [str, pathlib.Path] = sys.argv[8]  # 方差齐性检验结果
	filter_file: [str, pathlib.Path] = sys.argv[9]  # 过滤文件检验结果


if __name__ == '__main__':
	main()
