# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/20  22:07
# 名称：haplotype_to_phenotype.PY
# 工具：PyCharm
# 关联表型和基因型

# 运行：

'''
输入
$ head Glyma.20G250200_haplotype.txt
NJAU_C001 NJAU_C001 0 0 0 -9 AAGATCT
NJAU_C002 NJAU_C002 0 0 0 -9 AAGATCT
NJAU_C003 NJAU_C003 0 0 0 -9 CGTGTCG
NJAU_C004 NJAU_C004 0 0 0 -9 CGTGTCG
NJAU_C005 NJAU_C005 0 0 0 -9 CGTRTCG
NJAU_C006 NJAU_C006 0 0 0 -9 CGTGYYG
NJAU_C007 NJAU_C007 0 0 0 -9 CGTGTCG
NJAU_C008 NJAU_C008 0 0 0 -9 AAGAYCT
NJAU_C009 NJAU_C009 0 0 0 -9 CGTGTCG
NJAU_C010 NJAU_C010 0 0 0 -9 CATATCT

$ head Pro_content.txt
Taxa    2015yzBL        2016yzBL        2017yzBL
NJAU_C001       43.08   44.23   41.66
NJAU_C002       43.51   45.92   43.65
NJAU_C003       40.29   43.67   41.39
NJAU_C004       47.16   43.91   44.21
NJAU_C005       46.86   48.67   47.49
NJAU_C006       44.8    44.34   44.84
NJAU_C007       44.58   47.23   44.58
NJAU_C008       40.13   43.14   41.76
NJAU_C009       48.93   49.29   48.82
'''

'''
输出
$ head Glyma.20G250200_Pro_2015_hap2phe.txt
NJAU_C001       AAGATCT 43.08
NJAU_C002       AAGATCT 43.51
NJAU_C003       CGTGTCG 40.29
NJAU_C004       CGTGTCG 47.16
NJAU_C005       CGTRTCG 46.86
NJAU_C006       CGTGYYG 44.8
NJAU_C007       CGTGTCG 44.58
NJAU_C008       AAGAYCT 40.13
NJAU_C009       CGTGTCG 48.93
NJAU_C010       CATATCT 42.97
'''
import sys
import pandas as pd


def main():
	haplotype_df = pd.read_table(sys.argv[1], header=None, sep=" ")  # 单倍型数据
	content_df = pd.read_table(sys.argv[2])  # 表型数据
	year_flag = sys.argv[3]  # 年份
	gene_accession = sys.argv[4]  # 基因号
	phenotype = sys.argv[5]  # 表型
	
	# 合并两个表
	new_df = content_df[["Taxa", year_flag]].merge(haplotype_df.iloc[:][6], left_on="Taxa",
	                                               right_on=haplotype_df.iloc[:][0])
	new_df.to_csv(f"{gene_accession}_{phenotype}_{year_flag}_hap2phe.csv")


if __name__ == '__main__':
	main()
