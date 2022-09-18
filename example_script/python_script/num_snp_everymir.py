#python $scripts/num_snp_everymir.py haplotype_dir.txt num_snp_everymir.txt num_snp_final.txt

import sys

len_mir = {}
for line in open(sys.argv[1],"r"):
    l = line.strip().split("/")
    name = l[1]
    n=0
    for aaa in open(line.strip(),"r"):
        if n==0:
            a1 = aaa.strip().split(" ")
            hap = a1[6]
            lenth = len(hap)
            if name not in len_mir.keys():
                len_mir[name] = lenth
                break
            
        n+=1

dir2 = sorted(len_mir.items(), key=lambda item:item[1],reverse=False)

num = {}
file1 = []
for k,v in dir2:
    file1.append(k+"\t"+str(v)+"\n")
    if v not in num.keys():
        num[v] = 1
    else:
        num[v]+=1

file2 = []
for k2,v2 in num.items():
    file2.append(str(k2)+"snp"+"\t"+str(v2)+"\n")

w1 = open(sys.argv[2],"w")
w1.writelines(file1)
w2 = open(sys.argv[3],"w")
w2.writelines(file2)