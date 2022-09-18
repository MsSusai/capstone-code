# python $scripts/get_hap2phe_anova.py ${i}_${j}_hap2phe.txt

import sys 

print ("Type\tHap\tSample\tValue")

phy = {}
hap = {}
for line in open(sys.argv[1],"r"):
    l = line.strip().split("\t")
    phy[l[0]] = l[2]
    if l[1] not in hap.keys():
        hap[l[1]] = [l[0]]
    else:
        hap[l[1]].append(l[0])

n=1
for k,v in hap.items():
    ll = "hap"+str(n)
    for i in v:
        if i in phy.keys():
            print (ll+"\t"+k+"\t"+i+"\t"+phy[i])
    n+=1
    