# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/27  16:42 
# 名称：anova.PY
# 工具：PyCharm
# 检验数据正态分布（kstest，p>0.05）、方差齐性（levene,p>0.01）最后做方差分析（F），多重比较（p<0.05）

import sys

import pandas as pd
import numpy as np

from scipy.stats import kstest
from scipy.stats import levene
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd


