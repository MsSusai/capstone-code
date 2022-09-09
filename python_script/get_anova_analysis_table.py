#python get_anova_analysis_table.py ${j}_haplotype.txt Grain_weight.txt ${n} > anova_${j}_${n}_GW.txt
import sys

print ("Type\tHap\tSample\tValue")

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

hap = {}
for line in open(sys.argv[1],"r"):
    l = line.strip().split(" ")
    if l[-1] not in hap.keys():
        hap[l[-1]] = [l[0]]
    else:
        hap[l[-1]].append(l[0])

m=1
for k,v in hap.items():
    ll = "hap"+str(m)
    for i in v:
        if i in phe.keys():
            print (ll+"\t"+k+"\t"+i+"\t"+phe[i])
    m+=1
