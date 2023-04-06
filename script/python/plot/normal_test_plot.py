# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2022/11/2  21:30 
# 名称：normal_test_plot.py
# 工具：PyCharm

from plotnine import *
import patchworklib as pw
import pandas as pd
from scipy.stats import kstest

data = pd.read_table("../../../phenotype/grain_weight.txt")

stat2015, ks_value_2015 = kstest(data["2015"].dropna(axis=0), 'norm',
                                 (data["2015"].mean(), data["2015"].std()))
stat2016, ks_value_2016 = kstest(data["2016"].dropna(axis=0), 'norm',
                                 (data["2016"].mean(), data["2016"].std()))
stat2017, ks_value_2017 = kstest(data["2017"].dropna(axis=0), 'norm',
                                 (data["2017"].mean(), data["2017"].std()))
ks_value_2015 = round(ks_value_2015, 3)
ks_value_2016 = round(ks_value_2016, 3)
ks_value_2017 = round(ks_value_2017, 3)

plot2015 = ggplot(data, aes(sample="2015")) \
           + geom_qq() \
           + geom_qq_line() \
           + ylab("2015") \
           + theme(plot_title=element_text(face="bold", size=14), ) \
           + ggtitle("Grain Weight Normality Test\n"
                     f"\nKolmogorov-Smirnov test value: {ks_value_2015}")

plot2016 = ggplot(data, aes(sample="2016")) \
           + geom_qq() \
           + geom_qq_line() \
           + ylab("2016") \
           + theme(plot_title=element_text(face="bold", size=14), ) \
           + ggtitle("Grain Weight Normality Test\n"
                     f"\nKolmogorov-Smirnov test value: {ks_value_2016}")

plot2017 = ggplot(data, aes(sample="2017")) \
           + geom_qq() \
           + geom_qq_line() \
           + ylab("2017") \
           + theme(plot_title=element_text(face="bold", size=14), ) \
           + ggtitle("Grain Weight Normality Test\n"
                     f"\nKolmogorov-Smirnov test value: {ks_value_2017}")

g1 = pw.load_ggplot(plot2015, figsize=(3, 3))
g2 = pw.load_ggplot(plot2016, figsize=(3, 3))
g3 = pw.load_ggplot(plot2017, figsize=(3, 3))

g123 = (g1 | g2 | g3)
g123.savefig("grain_weight.png")
