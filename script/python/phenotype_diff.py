# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2022/12/1  19:27 
# 名称：phenotype_diff.py
# 工具：PyCharm
import pandas as pd
import os

phenotype_path = r"../../result/phenotype/"
files = os.listdir(phenotype_path)

for file in files:
    filename = file[:-4]
    phenotype_file = pd.read_table(phenotype_path + file)
    # print(phenotype_file)
    # print(phenotype_file)
    phe_2015_mean = phenotype_file["2015"].dropna(axis=0).mean()
    phe_2016_mean = phenotype_file["2016"].dropna(axis=0).mean()
    # phe_2017_mean = phenotype_file["2017"].dropna(axis=0).mean()
    total_mean = (phe_2015_mean + phe_2016_mean) / 2
    per10 = total_mean * 0.10
    per20 = total_mean * 0.20
    per30 = total_mean * 0.30
    per40 = total_mean * 0.40


    phenotype_file = phenotype_file[phenotype_file["Average"] - total_mean > 0] # >0正表型 <0负表型
    # print(len(phenotype_file))

    # 负表型前加abs()
    # 例：per10_20 = phenotype_file[abs(phenotype_file["Average"] - total_mean) > per10]
    per_10 = phenotype_file[phenotype_file["Average"] - total_mean < per10]

    per10_20 = phenotype_file[phenotype_file["Average"] - total_mean > per10]
    per10_20 = per10_20[phenotype_file["Average"] - total_mean < per20]

    per20_30 = phenotype_file[phenotype_file["Average"] - total_mean > per20]
    per20_30 = per20_30[phenotype_file["Average"] - total_mean < per30]

    per30_40 = phenotype_file[phenotype_file["Average"] - total_mean > per30]
    per30_40 = per30_40[phenotype_file["Average"] - total_mean < per40]

    per_40 = phenotype_file[phenotype_file["Average"] - total_mean > per40]

    # print(len(per_10))
    # print(len(per10_20))
    # print(len(per20_30))
    # print(len(per30_40))
    # print(len(per_40))
    # print("-----------")
    per_10.to_csv(f"{filename}_10.csv")
    per10_20.to_csv(f"{filename}_10_20.csv")
    per20_30.to_csv(f"{filename}_20_30.csv")
    per30_40.to_csv(f"{filename}_30_40.csv")
    per_40.to_csv(f"{filename}_40.csv")



