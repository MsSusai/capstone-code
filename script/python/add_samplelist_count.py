# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2022/11/10  15:33 
# 名称：add_samplelist_count.py
# 工具：PyCharm
import pandas as pd
import os

countlist = []

path = "../../result/hap/"
files = os.listdir(path)
for file in files:
    filepath = path + file
    df = pd.read_csv(filepath)
    for line in df["Sample List"]:
        count = line.split(',')
        countlist.append(len(count))
    df["Sample Count"] = countlist
    countlist = []
    df.to_csv(file)
