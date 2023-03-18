# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/9/20  22:07
# 名称：haplotype_to_phenotype.PY
# 工具：PyCharm
# 关联表型和基因型，并列出单倍型

# 运行：
# windows: python .\my_script\python\new\new_haplotype_to_phenotype.py .\sample_file\Glyma.01G001700_haplotype.txt .\sample_file\protein.txt Glyma.01G001700 protein

'''
输入
$ head Glyma.01G001700_haplotype.txt
CS001 CS001 0 0 0 -9 GT
CS002 CS002 0 0 0 -9 GT
CS003 CS003 0 0 0 -9 GT
CS004 CS004 0 0 0 -9 GT
CS005 CS005 0 0 0 -9 GT
CS006 CS006 0 0 0 -9 GT
CS007 CS007 0 0 0 -9 GT
CS008 CS008 0 0 0 -9 GT
CS009 CS009 0 0 0 -9 GT
CS010 CS010 0 0 0 -9 GT

$ head protein.txt
CS002	46.6
CS004	44.1
CS005	45.6
CS006	43.9
CS007	41.1
CS008	44.2
CS009	43.6
CS010	43.9
'''

'''
输出
$ head Glyma.01G001700_protein_hap2phe.txt
,sample,value,haplotype,type
0,CS002,46.6,GT,hap1
1,CS004,44.1,GT,hap1
2,CS005,45.6,GT,hap1
3,CS006,43.9,GT,hap1
4,CS007,41.1,GT,hap1
5,CS008,44.2,GT,hap1
6,CS009,43.6,GT,hap1
7,CS010,43.9,GT,hap1
8,CS011,42.1,GT,hap1
9,CS012,44.0,GT,hap1
10,CS013,42.2,GT,hap1
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
    content_df: pd.DataFrame = pd.read_table(sys.argv[2], header=None)  # 表型数据
    gene_accession: str = sys.argv[3]  # 基因号
    phenotype: str = sys.argv[4]  # 表型
    haplotype: dict = define_haptype(haplotype_df)  # 单倍型

    # print(f"正在关联{gene_accession}基因表型和基因型")

    # 合并两个表
    new_df = content_df.merge(haplotype_df.iloc[:][6], left_on=0,
                              right_on=haplotype_df.iloc[:][0])

    new_df['type'] = None  # 创造单倍型type新列

    for key, value in haplotype.items():
        new_df.type[new_df[6] == key] = value  # 赋予单倍型

    new_df.rename(columns={6: 'haplotype', 0: 'sample', 1: "value"},
                  inplace=True)  # 修改表头

    new_df.to_csv(f"{gene_accession}_{phenotype}_hap2phe.csv")  # 输出


if __name__ == '__main__':
    main()
