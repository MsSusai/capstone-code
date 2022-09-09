# python $scripts/get_haplotype.py Osa-MIR10519_range.ped Osa-MIR10519_haplotype.txt

import sys

dir={"AG":"R","GC":"S","GT":"K","AC":"M","AT":"W","TC":"Y"}

for line in open(sys.argv[1],"r"):
    l = line.strip().split(" ")
    string = l[:6]
    haplotype = ""
    for i in range(6,len(l)):
        if i%2==0:
            if l[i]!="0":
                if l[i]==l[i+1]:
                    haplotype+=l[i]
                else:
                    if l[i]+l[i+1] in dir.keys():
                        haplotype+=dir[l[i]+l[i+1]]
                    elif l[i+1]+l[i] in dir.keys():
                        haplotype+=dir[l[i+1]+l[i]]
            else:
                haplotype+="-"        
        else:
            pass
    string.append(haplotype)
    print (" ".join(string))
       