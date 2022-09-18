# python $scripts/get_haplotype_phenotype.py ${i}_haplotype.txt $phenotype/${j}.txt ${j}>

import sys

flag = sys.argv[3]
phe = {}
n=0
for line in open(sys.argv[2],"r"):
    l = line.strip().split("\t")
    if n==0:
        if flag==l[1][:4]:
            index = 1
        elif flag==l[2][:4]:
            index = 2
        elif flag==l[3][:4]:
            index = 3
    else:
        if l[index]!="NA":
            phe[l[0]] = l[index]
    n+=1

for line in open(sys.argv[1],"r"):
    l = line.strip().split(" ")
    if l[0] in phe.keys():
        print (l[0]+"\t"+l[-1]+"\t"+phe[l[0]])
    else:
        pass