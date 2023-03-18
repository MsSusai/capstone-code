# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2022/12/6  21:14 
# 名称：anova_data.py
# 工具：PyCharm
# 将anova结果提取出来为csv，供数据库使用

import sys
import pandas as pd

anova_path = sys.argv[1]
gene_loc = sys.argv[2]
phenotype = sys.argv[3]
outputpath = sys.argv[4]

anova_data = pd.read_table(anova_path, keep_default_na=False)

col = ["name", "sum_sq", "df", "F", "PR(>F)"]
anova_data.columns = col
anova_data["loc"] = gene_loc
anova_data["trait"] = phenotype
anova_data.to_csv(outputpath, mode="a+", index=False, header=False)
