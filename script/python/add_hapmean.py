# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2023/3/19  10:23 
# 名称：add_hapmean.py
# 工具：PyCharm
# 在数据库hapdata表格后添加一列记录出现的原始数值

import sys
import pandas as pd

inputpath = sys.argv[1]
happath_2016 = sys.argv[2]
gene_loc = sys.argv[3]
outputpath = sys.argv[4]

hapdata_2016 = pd.read_csv(happath_2016).dropna(axis=0)
inputdata = pd.read_csv(inputpath)

locdf = inputdata[inputdata["LOC"] == gene_loc]
haplotype_list = locdf["Haplotypes"].tolist()
# print(haplotype_list)
for hap in haplotype_list:
    value = hapdata_2016[hapdata_2016["type"] == hap]["value"].tolist()
    values = [str(i) for i in value] # float转str
    newdf = locdf[locdf["Haplotypes"] == hap]
    newdf["values"] = ','.join(values)
    # print(newdf)
    newdf.to_csv(outputpath, mode="a+", index=False, header=False)