# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/18  20:04 
# 名称：haplotype.PY
# 工具：PyCharm
# 获取单倍型

# for gene in $(cat snp_gene_name.txt)
# 运行：python /home/riceUsers/lhr/soybean/src/my_script/python_script/haplotype.py /home/riceUsers/lhr/soybean/temp_file/single/$gene.ped > /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt
# nohup sh run_haplotype.sh > run_haplotype.log 2>&1 &
'''
输入
(base) lhr@huangji-5885H-V5:~/soybean/temp_file/single$ head Glyma.01G000100.ped
NJAU_C001 NJAU_C001 0 0 0 -9 T T G G
NJAU_C002 NJAU_C002 0 0 0 -9 T T G G
NJAU_C003 NJAU_C003 0 0 0 -9 T T G G
NJAU_C004 NJAU_C004 0 0 0 -9 T T G G
NJAU_C005 NJAU_C005 0 0 0 -9 A A A A
NJAU_C006 NJAU_C006 0 0 0 -9 T T G G
NJAU_C007 NJAU_C007 0 0 0 -9 A A A A
NJAU_C008 NJAU_C008 0 0 0 -9 A A A A
NJAU_C009 NJAU_C009 0 0 0 -9 T T G G
NJAU_C010 NJAU_C010 0 0 0 -9 A A A A
'''

'''
输出
NJAU_C001 NJAU_C001 0 0 0 -9 TG
NJAU_C002 NJAU_C002 0 0 0 -9 TG
NJAU_C003 NJAU_C003 0 0 0 -9 TG
NJAU_C004 NJAU_C004 0 0 0 -9 TG
NJAU_C005 NJAU_C005 0 0 0 -9 AA
NJAU_C008 NJAU_C008 0 0 0 -9 AA
NJAU_C009 NJAU_C009 0 0 0 -9 TG
NJAU_C010 NJAU_C010 0 0 0 -9 AA
'''

import sys


def main():
	dir = {"AG": "R", "GA": "R",
	       "GC": "S", "CG": "S",
	       "GT": "K", "TG": "K",
	       "AC": "M", "CA": "M",
	       "AT": "W", "TA": "W",
	       "TC": "Y", "CT": "Y"}  # 兼并碱基表示
	for line in open(sys.argv[1], "r"):
		haplotype_line = line.strip().split(" ")  # 分割每一行
		# print(haplotype_line)
		haplotype = ""
		string = haplotype_line[:5 + 1]  # 取前面的注释
		
		for i in range(6, len(haplotype_line), 2):  # 从第六位开始是父母本碱基
			if "0" not in (haplotype_line[i], haplotype_line[i + 1]):  # 0为缺失
				if haplotype_line[i] == haplotype_line[i + 1]:  # 纯合
					haplotype += haplotype_line[i]
				elif haplotype_line[i] + haplotype_line[i + 1] in dir.keys():  # 杂合
					haplotype += dir[haplotype_line[i] + haplotype_line[i + 1]]
			else:
				haplotype += "-"
		
		string.append(haplotype)
		print(" ".join(string))


if __name__ == '__main__':
	main()
