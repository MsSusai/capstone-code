# python $scripts/get_trans_range.py ${i} /home/riceUsers/zxa/genomefile/MSU7/rice/rice_all.gff3 


import sys

gene = sys.argv[1]

genename = ""
for line in open(sys.argv[2],"r"):
    if line.startswith("#"):
        pass
    else:
        if line.strip()!="":
            l = line.strip().split("\t")
            chr = ""
            if len(l[0])==4:
                chr = l[0][-1]
            else:
                chr = l[0][-2:]
            if l[2] == "gene":
                for i in l[-1].split(";"):
                    if i.startswith("Name="):
                        genename = i.split("=")[1]
            if genename==gene:
                if l[2] == "CDS":
                    for i in l[-1].split(";"):
                        if i.startswith("Parent"):
                            trans = i.split("=")[1]
                            print chr+"\t"+l[3]+"\t"+l[4]+"\t"+trans
                
                
            
        