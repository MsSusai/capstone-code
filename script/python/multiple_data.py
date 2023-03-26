# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2022/12/6  20:37 
# 名称：multiple_data.py
# 工具：PyCharm
# 将多重比较结果提取出来为csv，供数据库使用

import sys
import pandas as pd

multpath_2015 = sys.argv[1]
multpath_2016 = sys.argv[2]
multpath_2017 = sys.argv[3]
gene_loc = sys.argv[4]
phenotype = sys.argv[5]
outputpath = sys.argv[6]

multdata2015 = pd.read_csv(multpath_2015, keep_default_na=False)
multdata2016 = pd.read_csv(multpath_2016, keep_default_na=False)
# multdata2017 = pd.read_csv(multpath_2017, keep_default_na=False)

hap2015 = multdata2015[multdata2015["reject"] == True]
hap2016 = multdata2016[multdata2016["reject"] == True]
# hap2017 = multdata2017[multdata2017["reject"] == True]
hapmergedf = hap2016.merge(hap2015, on=["group1", "group2", "reject"])
# hapmergedf = hapmergedf.merge(hap2017, on=["group1", "group2", "reject"])
hapmergedf["loc"] = gene_loc
hapmergedf["trait"] = phenotype
newhapdf = pd.DataFrame(hapmergedf,
                        columns=["loc", "trait", "group1", "group2", "meandiff_x", "p-adj_x", "lower_x", "upper_x", "reject"])
# print(hapmergedf)
# print(hap2016)
# print(newhapdf)
newhapdf.to_csv(outputpath, mode="a+", index=False, header=False)
