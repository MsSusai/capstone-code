# python get_phy_mean.py all.txt Protein_content.txt Oil_content.txt Wsp_content.txt 

import sys


n=0
stringall_pro=[]
stringall_oil=[]
stringall_wsp=[]
for line in open(sys.argv[1],"r"):
    if n>1:
        l = line.strip().split("\t")
        num = l[0]
        name = ""
        if len(num)==1:
            name = "NJAU_C00"+str(num)
        elif len(num)==2:
            name = "NJAU_C0"+str(num)
        else:
            name = "NJAU_C"+str(num)
        string = []
        for i in range(1,27,3):
            # print (i)
            nn=0
            rep1 = l[i]
            rep2 = l[i+1]
            rep3 = l[i+2]
            if rep1=="" or rep1==".":
                nn+=1
                rep1 = 0
            if rep2=="" or rep2==".":
                nn+=1
                rep2 = 0
            if rep3=="" or rep3==".":
                nn+=1
                rep3 = 0
            if nn==3:
                mean="NA"
            if nn==2:
                mean = round((float(rep1)+float(rep2)+float(rep3))/1,2)
            if nn==1:
                mean = round((float(rep1)+float(rep2)+float(rep3))/2,2)
            if nn==0:
                mean = round((float(rep1)+float(rep2)+float(rep3))/3,2)
            string.append(str(mean))
        stringall_1=name+"\t"+"\t".join(string[:3])
        stringall_2=name+"\t"+"\t".join(string[3:6])
        stringall_3=name+"\t"+"\t".join(string[6:9])
        stringall_pro.append(stringall_1)
        stringall_oil.append(stringall_2)
        stringall_wsp.append(stringall_3)
    n+=1

# print (stringall)

title="Taxa\t2015yzBL\t2016yzBL\t2017yzBL\n"
w1 = open(sys.argv[2],"w")
w1.writelines(title)
w1.writelines("\n".join(stringall_pro))
w2 = open(sys.argv[3],"w")
w2.writelines(title)
w2.writelines("\n".join(stringall_oil))
w3 = open(sys.argv[4],"w")
w3.writelines(title)
w3.writelines("\n".join(stringall_wsp))

