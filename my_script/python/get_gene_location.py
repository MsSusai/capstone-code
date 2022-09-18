# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/13  20:59 
# 名称：get_gene_location.PY
# 工具：PyCharm
# 从gene注释文件中提取所有gene的位置

# 运行
# python /home/riceUsers/lhr/soybean/src/my_python_script/get_gene_location.py > /home/riceUsers/lhr/soybean/temp_file/gene_location.txt

# 注释文件
# /home/riceUsers/lhr/soybean/genomefile/Gmax_275_Wm82.a2.v1.gene.gff3

'''
输入
#gff-version 3
#annot-version Wm82.a2.v1
Chr01   phytozomev10    gene    27355   28320   .       -       .       ID=Glyma.01G000100.Wm82.a2.v1;Name=Glyma.01G000100;ancestorIdentifier=Glyma01g00210.v1.1
Chr01   phytozomev10    mRNA    27355   28320   .       -       .       ID=Glyma.01G000100.1.Wm82.a2.v1;Name=Glyma.01G000100.1;pacid=30544134;longest=1;Parent=Glyma.01G000100.Wm82.a2.v1
Chr01   phytozomev10    CDS     28139   28218   .       -       0       ID=Glyma.01G000100.1.Wm82.a2.v1.CDS.1;Parent=Glyma.01G000100.1.Wm82.a2.v1;pacid=30544134
Chr01   phytozomev10    five_prime_UTR  28219   28320   .       -       .       ID=Glyma.01G000100.1.Wm82.a2.v1.five_prime_UTR.1;Parent=Glyma.01G000100.1.Wm82.a2.v1;pacid=30544134
Chr01   phytozomev10    CDS     27926   27991   .       -       1       ID=Glyma.01G000100.1.Wm82.a2.v1.CDS.2;Parent=Glyma.01G000100.1.Wm82.a2.v1;pacid=30544134
Chr01   phytozomev10    three_prime_UTR 27355   27655   .       -       .       ID=Glyma.01G000100.1.Wm82.a2.v1.three_prime_UTR.1;Parent=Glyma.01G000100.1.Wm82.a2.v1;pacid=30544134
Chr01   phytozomev10    CDS     27656   27824   .       -       1       ID=Glyma.01G000100.1.Wm82.a2.v1.CDS.3;Parent=Glyma.01G000100.1.Wm82.a2.v1;pacid=30544134
Chr01   phytozomev10    gene    58975   67527   .       -       .       ID=Glyma.01G000200.Wm82.a2.v1;Name=Glyma.01G000200
'''

'''
输出
1       28139   28218   Glyma.01G000100.1.Wm82.a2.v1.CDS.1      Glyma.01G000100
1       27926   27991   Glyma.01G000100.1.Wm82.a2.v1.CDS.2      Glyma.01G000100
1       27656   27824   Glyma.01G000100.1.Wm82.a2.v1.CDS.3      Glyma.01G000100
1       64055   64061   Glyma.01G000200.1.Wm82.a2.v1.CDS.1      Glyma.01G000200
1       63334   63417   Glyma.01G000200.1.Wm82.a2.v1.CDS.2      Glyma.01G000200
1       63066   63141   Glyma.01G000200.1.Wm82.a2.v1.CDS.3      Glyma.01G000200
1       62567   62644   Glyma.01G000200.1.Wm82.a2.v1.CDS.4      Glyma.01G000200
1       62006   62045   Glyma.01G000200.1.Wm82.a2.v1.CDS.5      Glyma.01G000200
'''

def main():
	gff3_file = "/home/riceUsers/lhr/soybean/genomefile/Gmax_275_Wm82.a2.v1.gene.gff3"
	for line in open(gff3_file, 'r'):
		# 去掉最开头的注释
		if line.startswith("#"):
			pass
		else:
			if line.strip() is not None:  # 开头和结尾没有空格
				single_gene = line.strip().split("\t")  # 分割单行
				if single_gene[2] == "CDS":  # 只要CDS区域
					start = single_gene[3]
					end = single_gene[4]
					if single_gene[0][-2] == "0":
						chr = single_gene[0][-1]  # 染色体编号01-09
					elif single_gene[0][-2] == "1" or single_gene[0][-2] == "2":
						chr = single_gene[0][-2:]  # 染色体编号10-20
					for split in single_gene[-1].split(";"):
						if split.startswith("ID"):
							id = split.split("=")[1]
							gene_name = id.split(".")[0] + "." + id.split(".")[1]
							print(chr + "\t" + start + "\t" + end + "\t" + id + "\t" + gene_name)


if __name__ == '__main__':
	main()
