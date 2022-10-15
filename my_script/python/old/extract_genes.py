# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/10/5  19:48 
# 名称：extract_genes.PY
# 工具：PyCharm
# 统计基因个数，提取三年都有的基因

import os
import re

set2015 = set()
set2016 = set()
set2017 = set()
total2015 = 0
total2016 = 0
total2017 = 0

files = os.listdir(r"../../../anova_result_no_normaltest")
file_name = [file for file in files if "multiple_comparison" in file]
phenotype = ["grain_weight", "oil_content", "protein_content", "water_soluble_protein"]
for phe in phenotype:
	for name in file_name:
		if phe in name:
			for line in open(f"../../../anova_result_no_normaltest/{name}", "r"):
				# print(re.search("Glyma\.[0-9]{2}G[0-9]{6}", line.strip()))
				if "2015" in name:
					search = re.search("Glyma\.[0-9]{2}G[0-9]{6}", line.strip())
					if search is not None:
						set2015.add(search.group())
						total2015 += 1
				elif "2016" in name:
					search = re.search("Glyma\.[0-9]{2}G[0-9]{6}", line.strip())
					if search is not None:
						set2016.add(search.group())
						total2016 += 1
				elif "2017" in name:
					search = re.search("Glyma\.[0-9]{2}G[0-9]{6}", line.strip())
					if search is not None:
						set2017.add(search.group())
						total2017 += 1
	
	genes = set2015 & set2016 & set2017
	print(phe)
	print(genes)
	print(len(genes))
	with open(f"{phe}_genes.txt", "w") as f:
		f.write(f"{phe}  total:{len(genes)}  2015:{total2015}  2016:{total2016}  2017:{total2017}\n")
		f.write("\n".join(genes))
	set2015.clear()
	set2016.clear()
	set2017.clear()
	total2015 = total2016 = total2017 = 0
