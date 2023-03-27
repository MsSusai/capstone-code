# -*- encoding: utf-8 -*-

# 作者：Sosai
# 时间：2022/10/31  20:12 
# 名称：hapdata_for_database.py
# 工具：PyCharm

import sys
import pandas as pd

happath_2015 = sys.argv[1]
happath_2016 = sys.argv[2]
happath_2017 = sys.argv[3]
multpath_2015 = sys.argv[4]
multpath_2016 = sys.argv[5]
multpath_2017 = sys.argv[6]
gene_loc = sys.argv[7]
phenotype = sys.argv[8]
outputpath = sys.argv[9]

hapdata_2015 = pd.read_csv(happath_2015).dropna(axis=0)
hapdata_2016 = pd.read_csv(happath_2016).dropna(axis=0)
# hapdata_2017 = pd.read_csv(happath_2017).dropna(axis=0)

multdata2015 = pd.read_csv(multpath_2015)
multdata2016 = pd.read_csv(multpath_2016)
# multdata2017 = pd.read_csv(multpath_2017)

hap2015 = multdata2015[multdata2015["reject"] == True]
hap2016 = multdata2016[multdata2016["reject"] == True]
# hap2017 = multdata2017[multdata2017["reject"] == True]

hapdict = {}
hapmergedf = hap2016.merge(hap2015, on=["group1", "group2", "reject"])
# hapmergedf = hapmergedf.merge(hap2017, on=["group1", "group2", "reject"])
if not hapmergedf.empty:
    hapgroup1 = hapmergedf["group1"]
    hapgroup2 = hapmergedf["group2"]
    for hap1, hap2 in zip(hapgroup1, hapgroup2):
        # hap1mean = round((hapdata_2015[hapdata_2015["type"] == hap1]["value"].mean() +
        #                   hapdata_2016[hapdata_2016["type"] == hap1]["value"].mean() +
        #                   hapdata_2017[hapdata_2017["type"] == hap1]["value"].mean()) / 3, 3)
        hap1mean = round((hapdata_2015[hapdata_2015["type"] == hap1]["value"].mean() +
                          hapdata_2016[hapdata_2016["type"] == hap1]["value"].mean()) / 2, 3)
        # hap2mean = round((hapdata_2015[hapdata_2015["type"] == hap2]["value"].mean() +
        #                   hapdata_2016[hapdata_2016["type"] == hap2]["value"].mean() +
        #                   hapdata_2017[hapdata_2017["type"] == hap2]["value"].mean()) / 3, 3)
        hap2mean = round((hapdata_2015[hapdata_2015["type"] == hap2]["value"].mean() +
                          hapdata_2016[hapdata_2016["type"] == hap2]["value"].mean()) / 2, 3)
        hap1snp = hapdata_2015[hapdata_2015["type"] == hap1]["haplotype"].iloc[0]
        hap2snp = hapdata_2015[hapdata_2015["type"] == hap2]["haplotype"].iloc[0]
        sample1 = hapdata_2015[hapdata_2015["type"] == hap1]["sample"].values.tolist()
        sample2 = hapdata_2015[hapdata_2015["type"] == hap2]["sample"].values.tolist()
        if hap1 not in hapdict.keys():
            hapdict[hap1] = [hap1snp, hap1mean, sample1]
        if hap2 not in hapdict.keys():
            hapdict[hap2] = [hap2snp, hap2mean, sample2]

"""
{'hap1': ['GCAGAC', 20.682, ['NJAU_C001', 'NJAU_C091', 'NJAU_C098', 'NJAU_C099', 'NJAU_C100', 'NJAU_C103', 'NJAU_C172', 'NJAU_C198', 'NJAU_C199', 'NJAU_C203', 'NJAU_C211', 'NJAU_C213']], 
'hap3': ['ACGAGT', 15.474, ['NJAU_C004', 'NJAU_C005', 'NJAU_C008', 'NJAU_C009', 'NJAU_C010', 'NJAU_C011', 'NJAU_C012', 'NJAU_C013', 'NJAU_C014', 'NJAU_C015', 'NJAU_C016', 'NJAU_C018', 'NJAU_C021', 'NJAU_C022', 'NJAU_C023', 'NJAU_C025', 'NJAU_C026', 'NJAU_C027', 'NJAU_C030', 'NJAU_C031', 'NJAU_C032', 'NJAU_C033', 'NJAU_C036', 'NJAU_C037', 'NJAU_C038', 'NJAU_C039', 'NJAU_C042', 'NJAU_C043', 'NJAU_C044', 'NJAU_C050', 'NJAU_C055', 'NJAU_C056', 'NJAU_C058', 'NJAU_C059', 'NJAU_C060', 'NJAU_C062', 'NJAU_C064', 'NJAU_C066', 'NJAU_C068', 'NJAU_C069', 'NJAU_C070', 'NJAU_C073', 'NJAU_C074', 'NJAU_C078', 'NJAU_C082', 'NJAU_C085', 'NJAU_C092', 'NJAU_C093', 'NJAU_C094', 'NJAU_C096', 'NJAU_C108', 'NJAU_C109', 'NJAU_C115', 'NJAU_C116', 'NJAU_C117', 'NJAU_C124', 'NJAU_C125', 'NJAU_C127', 'NJAU_C128', 'NJAU_C131', 'NJAU_C132', 'NJAU_C133', 'NJAU_C134', 'NJAU_C135', 'NJAU_C137', 'NJAU_C138', 'NJAU_C139', 'NJAU_C140', 'NJAU_C142', 'NJAU_C144', 'NJAU_C145', 'NJAU_C150', 'NJAU_C151', 'NJAU_C154', 'NJAU_C158', 'NJAU_C159', 'NJAU_C160', 'NJAU_C162', 'NJAU_C165', 'NJAU_C168', 'NJAU_C173', 'NJAU_C174', 'NJAU_C176', 'NJAU_C178', 'NJAU_C180', 'NJAU_C184', 'NJAU_C185', 'NJAU_C186', 'NJAU_C189', 'NJAU_C190', 'NJAU_C191', 'NJAU_C197', 'NJAU_C200', 'NJAU_C202', 'NJAU_C205', 'NJAU_C206', 'NJAU_C207', 'NJAU_C209', 'NJAU_C212', 'NJAU_C217', 'NJAU_C218', 'NJAU_C219']]}
"""
outputlist = []
for key, value in hapdict.items():
    outputlist.append([gene_loc, value[2], phenotype, key, value[0], value[1]])
outputdf = pd.DataFrame(outputlist, columns=["LOC", "Sample List", "Trait", "Haplotypes", "SNPs", "Mean"])
outputdf.to_csv(outputpath, mode="a+", index=False, header=False)
