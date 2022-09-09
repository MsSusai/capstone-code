# python $scripts/mean_hap2phe.py ${i}_hap2phe.txt ${j} ../${i}_range.map > ${i}_hap2phe_mean.txt

import sys

head = sys.argv[2]
position = open(sys.argv[3],"r")

pos = ""
for line in position:
    l = line.strip().split("\t")
    pos += l[-1]
    pos += "|"

print ("hapID"+"\t"+"hap"+"\t"+head+"\t"+pos+"\t"+"sample")
hap = {}
phy = {}
for line in open(sys.argv[1],"r"):
    l = line.strip().split("\t")
    if l[1] not in hap.keys():
        hap[l[1]] = [l[0]]
    else:
        hap[l[1]].append(l[0])
    if l[0] not in phy.keys():
        phy[l[0]] = l[2]

n = 1
for k,v in hap.items():
    all = 0
    for i in v:
        if i in phy.keys():
            all += float(phy[i])
    mean = format(all/len(v),'.2f')
    print ("hap"+str(n)+"\t"+k+"\t"+str(mean)+"\t"+str(len(v))+"\t"+",".join(v))
    n+=1   
      