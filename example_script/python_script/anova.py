# python $scripts/anova.py anova_Osa-MIR1122a_panicle_length.txt panicle_length Osa-MIR1122a

# python .\example_script\python_script\anova.py .\sample_file\anova_Glyma.09G057800_2016_Pro.txt Pro_content Glyma.09G057800_2016 .\sample_file\Pro_content.txt 0.05 normal_result_Glyma.09G057800_2016_Oil.txt variances_result_Glyma.09G057800_2016_Pro.txt filter_result_Glyma.09G057800_2016_Pro.txt

import sys
import numpy as np
from scipy.stats import kstest
from scipy.stats import levene
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# import pingouin as pg

df = pd.read_csv(sys.argv[1], header=0, index_col=None, sep="\t")
phy = sys.argv[2]
name = sys.argv[3]
phyfile = sys.argv[4]
flag = sys.argv[5]
output1 = sys.argv[6]
output2 = sys.argv[7]
output3 = sys.argv[8]

dir = {}
n = 0
for line in open(sys.argv[1], "r"):
	if n > 0:
		l = line.strip().split("\t")
		type = l[0]
		if type not in list(dir.keys()):
			dir[type] = [float(l[3])]
		else:
			dir[type].append(float(l[3]))
	n += 1
# print(df)
# print(dir)


m = 0
for line in open(phyfile, "r"):
	m += 1

print("flag=" + str(int(m) * float(flag)))# 保留不少于规定数目的单倍型

typenum = len(dir)
print(typenum)
nn = 0
for k, v in list(dir.items()):
	if len(v) >= int(m) * float(flag): # 保留不少于规定数目的单倍型（300*0.05=15）
		# if len(v)>=87:
		nn += 1
	else:
		del dir[k]

		df = df[~df['Type'].isin([k])]  # 将少于15个样本的单倍型剔除
print(dir)
print(len(dir))
cha = typenum - len(dir)

print(df)

filer = []
print("There are " + str(
	cha) + " haplotypes that contain less than 5 materials and are filtered, and the remaining " + str(
	len(dir)) + " haplotypes are used for subsequent analysis.")
filer.append("all: " + str(typenum) + "\n")
filer.append("filter: " + str(cha) + "\n")
filer.append("remain: " + str(len(dir)) + "\n")



if len(dir) > 1:
	final = []
	normalfile = []
	n = 0
	m = 0
	for v in list(dir.values()):
		value = np.array(v)
		test = kstest(value, 'norm')
		m += 1
		normalfile.append("kstest pvalue: " + str(test[1]) + "\n")
		if test[1] <= 0.05:
			n += 1
	print(normalfile)
	
	# mylist = []
	# # mylistk = []
	# # mylistv = []
	# string = []
	# levenes = []
	# head = ""
	# if m == n:
	# 	for v1 in list(dir.values()):
	# 		mylist.append(v1)
	# 	# print mylist
	# 	print(mylist)
		# for k1 in dir.keys():
		# for v1 in dir[k1]:
		# mylistv.append(v1)
		# mylistk.append(k1)
	# 	stat, p = levene(*mylist)
	# 	levenes.append("levene Fvalue: " + str(stat) + "\n")
	# 	levenes.append("levene pvalue: " + str(p) + "\n")
	# 	if p > 0.01:
	# 		model = ols('Value~C(Type)', data=df).fit()
	# 		anova_table = anova_lm(model, typ=2)
	# 		print(anova_table)
	# 		PR = anova_table.loc['C(Type)', 'PR(>F)']
	# 		F_value = anova_table.loc['C(Type)', 'F']
	# 		tablename = "./anova_table" + "_" + phy + "_" + name + ".txt"
	# 		anova_table.to_csv(tablename, sep="\t", na_rep="NA")
	# 		if PR < 0.05:
	# 			file1name = "./anova_result" + "_" + phy + "_" + name + ".txt"
	# 			file1 = open(file1name, "w")
	# 			file1.write("name\tphenotype\tgroup1\tgroup2\tF_value\tp_value\tmeandiff\tp-adj\n")
	# 			mc = pairwise_tukeyhsd(df['Value'], df['Type'], alpha=0.05)
	# 			print(df['Value'])
	# 			print(df['Type'])
	# 			# print mylistv
	# 			# print pd.Series(mylistv)
	#
	# 			# print pd.Series(mylistk)
	# 			# print mylistk
	# 			# mc = pairwise_tukeyhsd(pd.Series(mylistv),pd.Series(mylistk),alpha=0.05)
	#
	# 			# mc = MultiComparison(pd.Series(mylistv),pd.Series(mylistk))
	# 			# print mc
	# 			# tukey_result1 = mc.tukeyhsd(alpha = 0.05)
	# 			# print tukey_result1.summary()
	# 			print(mc)
	# 			tukey_result = mc._results_table.data[1:]
	# 			# print (tukey_result)
	# 			for line in tukey_result:
	# 				# if line[-1]=="True":
	# 				file1.write(name + "\t" + phy + "\t" + line[0] + "\t" + line[1] + "\t" + str(F_value) + "\t" + str(
	# 					PR) + "\t" + str(line[2]) + "\t" + str(line[3]) + "\n")
	# 			# print tukey_result
	# 			# print mc.summary()
	# 		else:
	# 			print("There is no difference in the average phenotype of the two haplotypes.")
# 		# else:
# 		# #filepath="/home/riceUsers/xueai/soybean/SNP/variance.txt"
# 		# #file=open(filepath,"a")
# 		# #file.writelines(name+"\n")
# 		# print("The variance between each group is not equal.")
# 		# print("We will use welch's anova.")
# 		# anova_table=pg.welch_anova(dv='Value',between='Type',data=df)
# 		# print(anova_table)
# 		# Pvalue = anova_table.iat[0,4]
# 		# print("Pvalue is "+str(Pvalue))
# 		# tablename = "./anova_table"+"_"+phy+"_"+name+"_variance.txt"
# 		# anova_table.to_csv(tablename,sep="\t",na_rep="NA")
# 		# if Pvalue<0.05:
# 		# result=pg.pairwise_gameshowell(dv='Value',between='Type',data=df)
# 		# print(result)
# 		# tablename2 = "./anova_result"+"_"+phy+"_"+name+"_variance.txt"
# 		# result.to_csv(tablename2,sep="\t",na_rep="NA")
# 		# else:
# 		# print("There is no difference in the average phenotype of the two haplotypes.")
# 	else:
# 		print("The data is not completely in accordance with the normal distribution.")
# 	w1 = open(output1, "w")
# 	w1.writelines(normalfile)
# 	w1.close()
#
# 	w2 = open(output2, "w")
# 	w2.writelines(levenes)
# 	w2.close()
# else:
# 	print("There is only 1 group of haplotypes or less, so the gene does not perform analysis of variance.")
#
# print(name + ".........finish!!!!!")

w3 = open(output3, "w")
w3.writelines(filer)
w3.close()
