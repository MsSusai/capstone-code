# python $scripts/get_material2hap.py ../../${i}_haplotype.txt anova_${i}_${j}_Pro.txt > ${i}_material_hap_${j}_Pro.txt

import sys

hapinfo = {}
cailiao = {}
for line in open(sys.argv[2],"r"):
    if line.startswith("Type"):
        pass
    else:
        l = line.strip().split("\t")
        name = l[0]+"/"+l[1]
        gw = l[2]+"/"+l[3]
        if l[1] not in hapinfo.keys():
            hapinfo[l[1]] = l[0]
        else:
            pass
        if name not in cailiao.keys():
            cailiao[name] = [gw]
        else:
            cailiao[name].append(gw)

num1 = {}
for line in open(sys.argv[1],"r"):
    l = line.strip().split(" ")
    if l[-1] in hapinfo.keys():
        type = hapinfo[l[-1]]
        if type not in num1.keys():
            n=1
            num1[type] = n
        else:
            num1[type]+=1


for k in cailiao.keys():
    hap = k.split("/")[0]
    seq = k.split("/")[1]
    if hap in num1.keys():
        a111 = num1[hap]
    all = 0.0
    m=0
    list1 = []
    for v in cailiao[k]:
        mat = v.split("/")[0]
        value = v.split("/")[1]
        all+=float(value)
        m+=1
        list1.append(mat)
    mean = round(all/m,2)
    string = str(mean)+"("+str(m)+"/"+str(a111)+")"
    print (hap+"\t"+seq+"\t"+string+"\t"+",".join(list1))
    