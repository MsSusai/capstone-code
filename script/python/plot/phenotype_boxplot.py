# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2023/3/28  15:46 
# 名称：phenotype_boxplot.py
# 工具：PyCharm

import os

from plotnine import *
# from lets_plot import *
from patchworklib import *
import pandas as pd

path = "../../../phenotype/"
files = os.listdir(path)
plotlist = []
g1234 = None

for file in files:
    filepath = path + file
    data = pd.read_table(filepath)
    # 箱线图
    col = data[['2015', '2016', '2017']].unstack().reset_index()  # 数据降维并重新索引
    col.columns = ['year', 'index', 'value']
    g = ggplot(col, aes(x='year', y='value')) \
        + geom_boxplot() \
        + ggtitle(f"{file[:-4]}") \
        + theme(plot_title=element_text(size=20, ha="center", margin={"b": 15}))
    # + scale_fill_manual(values=['dodgerblue', 'darkorange', 'limegreen'])
    # + geom_point(alpha=.1) \
    # + geom_jitter(width=.3, alpha=.5) \
    # ggsave(g, f"{file[:-4]}.png", dpi=300, width=4, height=4)

    # 相关系数热图
    # corr = data.corr().round(decimals=3).unstack().reset_index()
    # corr.columns = ['year1', 'year2', 'value']
    # g = ggplot(corr, aes(corr['year1'], corr['year2'])) \
    #     + geom_tile(aes(fill='value'), color='black') \
    #     + scale_fill_gradient(low='#E8D06C', high='#FF4E22') \
    #     + geom_text(aes(label=corr['value'])) \
    #     + ggtitle(f"{file[:-4]}") \
    #     + theme(axis_ticks=element_blank(), panel_background=element_blank(),
    #             plot_title=element_text(size=20, lineheight=10, vjust=0.5)) \
    #     + labs(x="", y="")
    plotlist.append(g)

g1 = load_ggplot(plotlist[0], figsize=(4, 4))
g2 = load_ggplot(plotlist[1], figsize=(4, 4))
g3 = load_ggplot(plotlist[2], figsize=(4, 4))
g4 = load_ggplot(plotlist[3], figsize=(4, 4))
g1234 = ((g1 + g2) / (g3 + g4))
g1234.savefig("boxplot.png")
