# python $scripts/get_every_mapped.py $genomefile/Gmax_275_Wm82.a2.v1.gene.gff3 genelocation_rangesnp.ped genelocation_rangesnp.map 

import sys
import os

gff=sys.argv[1]
map=sys.argv[2]
ped = sys.argv[3]

dir1 = {}
for line in open(gff,"r"):
    if line.startswith("#"):
        pass
    else:
        if line.strip() !="":
            l = line.strip().split("\t")
            if l[2]=="gene":
                start = l[3]
                end = l[4]
                chr = ""
                if l[0][-2]=="0":
                    chr = l[0][-1]
                else:
                    chr = l[0][-2:]
                genename = ""
                for i in l[-1].split(";"):
                    if i.startswith("Name"):
                        genename = i.split("=")[1] 
                # if genename=="Glyma.01G000100":
                for line2 in open(map,"r"):
                    ll = line2.strip().split("\t")
                    if ll[0]==chr and int(ll[-2])>=int(start) and int(ll[-2])<=int(end):
                        if genename not in dir1.keys():
                            dir1[genename] = [ll]
                        else:
                            dir1[genename].append(ll)

# print (dir1)
print (len(dir1))


for k in dir1.keys():
    filepath = './'+k+"/"+k+"_range.map"
    filepath2 = './'+k+"/"+k+"_range.ped"
    path = "/home/riceUsers/xueai/soybean/SNP/"+k
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    file = open(filepath,"w")
    file2 = open(filepath2,"w")
    indexs = []
    for v in dir1[k]:
        indexs.append(int(v[-1]))
        file.writelines("\t".join(v[:-1])+"\n")
    file.close()
    print (k+"mapfile finished!!!!")
    string = []
    for line in open(ped,"r"):
        l = line.strip().split(" ")
        top6 = " ".join(l[:6])
        for ind in indexs:
            top6+= " "+l[6:][ind*2]
            top6+= " "+l[6:][ind*2+1]
        string.append(top6)
    file2.writelines("\n".join(string))
    file2.close()
    print (k+"pedfile finished!!!!")
                
        
    
                    