# python $scripts/get_gene_location.py $genomefile/Gmax_275_Wm82.a2.v1.gene.gff3 gene_location_range.txt

import sys

gff3file=sys.argv[1]

for line in open(gff3file,"r"):
    if line.startswith("#"):
        pass
    else:
        if line.strip()!="":
            l = line.strip().split("\t")
            chr = ""
            start = l[3]
            end = l[4]
            # chain = l[6]
            if l[2]=="CDS":
                if len(l[0])==5:
                    if l[0][-2]=="0":
                        chr = l[0][-1]
                    else:
                        chr = l[0][-2:]
                    for i in l[-1].split(";"):
                        if i.startswith("ID"):
                            id = i.split("=")[1]
                            genename = id.split(".")[0]+"."+id.split(".")[1]
                            print (chr+"\t"+start+"\t"+end+"\t"+id+"\t"+genename)
