# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/20  22:07
# 名称：haplotype_to_phenotype.PY
# 工具：PyCharm
# 关联表型和基因型，并列出单倍型

# 运行：
# windows: python .\my_script\python\haplotype_to_phenotype.py .\sample_file\Glyma.20G250200_haplotype.txt .\sample_file\Pro_content.txt 2015yzBL Glyma.20G250200 protein
# linux: python /home/riceUsers/lhr/soybean/src/my_script/python_script/haplotype_to_phenotype.py /home/riceUsers/lhr/soybean/temp_file/single/${gene}_haplotype.txt /home/riceUsers/lhr/soybean/genomefile/${phenotype}.txt ${year} ${gene} ${phenotype}
'''
输入
$ head Glyma.20G250200_haplotype.txt
NJAU_C001 NJAU_C001 0 0 0 -9 AAGATCT
NJAU_C002 NJAU_C002 0 0 0 -9 AAGATCT
NJAU_C003 NJAU_C003 0 0 0 -9 CGTGTCG
NJAU_C004 NJAU_C004 0 0 0 -9 CGTGTCG
NJAU_C005 NJAU_C005 0 0 0 -9 CGTRTCG
NJAU_C006 NJAU_C006 0 0 0 -9 CGTGYYG
NJAU_C007 NJAU_C007 0 0 0 -9 CGTGTCG
NJAU_C008 NJAU_C008 0 0 0 -9 AAGAYCT
NJAU_C009 NJAU_C009 0 0 0 -9 CGTGTCG
NJAU_C010 NJAU_C010 0 0 0 -9 CATATCT

$ head Pro_content.txt
Taxa	2015yzBL	2016yzBL	2017yzBL
NJAU_C001	43.08	44.23	41.66
NJAU_C002	43.51	45.92	43.65
NJAU_C003	40.29	43.67	41.39
NJAU_C004	47.16	43.91	44.21
NJAU_C005	46.86	48.67	47.49
NJAU_C006	44.8	44.34	44.84
NJAU_C007	44.58	47.23	44.58
NJAU_C008	40.13	43.14	41.76
NJAU_C009	48.93	49.29	48.82
'''

'''
输出
$ head Glyma.20G250200_Pro_2015_hap2phe.txt
,sample,value,haplotype,type
0,NJAU_C001,43.08,AAGATCT,hap1
1,NJAU_C002,43.51,AAGATCT,hap1
2,NJAU_C003,40.29,CGTGTCG,hap2
3,NJAU_C004,47.16,CGTGTCG,hap2
4,NJAU_C005,46.86,CGTRTCG,hap3
5,NJAU_C006,44.8,CGTGYYG,hap4
6,NJAU_C007,44.58,CGTGTCG,hap2
7,NJAU_C008,40.13,AAGAYCT,hap5
8,NJAU_C009,48.93,CGTGTCG,hap2
9,NJAU_C010,42.97,CATATCT,hap6
10,NJAU_C012,43.11,CGTGYYG,hap4
'''
import sys
import pandas as pd


# 返回单倍型分类
def define_haptype(haplotype_df: pd.DataFrame) -> dict:
    haplotype: dict = {}
    i: int = 1
    for hap in haplotype_df.iloc[:][6]:
        if hap not in haplotype.keys():
            haplotype[hap] = "hap" + str(i)
            i += 1
    return haplotype


def main():
    haplotype_df: pd.DataFrame = pd.read_table(sys.argv[1], header=None, sep=" ")  # 单倍型数据
    content_df: pd.DataFrame = pd.read_table(sys.argv[2])  # 表型数据
    year_flag: str = sys.argv[3]  # 年份
    gene_accession: str = sys.argv[4]  # 基因号
    phenotype: str = sys.argv[5]  # 表型
    haplotype: dict = define_haptype(haplotype_df)  # 单倍型

    print(f"正在关联{gene_accession}基因表型和基因型")

    # 合并两个表
    new_df = content_df[["Taxa", year_flag]].merge(haplotype_df.iloc[:][6], left_on="Taxa",
                                                   right_on=haplotype_df.iloc[:][0])
    new_df['type'] = None  # 创造单倍型type新列

    for key, value in haplotype.items():
        new_df.type[new_df[6] == key] = value  # 赋予单倍型

    new_df.rename(columns={6: 'haplotype', 'Taxa': 'sample', year_flag: 'value'},
                  inplace=True)  # 修改表头

    new_df.to_csv(f"{gene_accession}_{phenotype}_{year_flag}_hap2phe.csv")  # 输出


if __name__ == '__main__':
	main()
