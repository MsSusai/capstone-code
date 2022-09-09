# python $scripts/get_freq.py ${i}_range.map ${i}_mafmiss.frq ${i}_mafmiss.lmiss > ${i}_frq_miss.txt

import sys

map = open(sys.argv[1],"r")
frq = open(sys.argv[2],"r")
miss = open(sys.argv[3],"r")

snpdir = {}
for line in map:
    l = line.strip().split()
    snp = l[1]
    position = l[3]
    snpdir[snp] = position

print ("Chr\tPosition\tAlt_nt\tMajor\tMAF\tMissing")
n=0
dir = {}
for line in frq:
    if n==0:
        pass
    else:
        l = line.strip().split()
        Chr = "chr"+l[0]
        snp = l[1]
        if snp in snpdir.keys():
            Position = snpdir[snp]
            Alt_nt = l[3]
            Major = l[2]
            MAF = l[4]
            dir[Position] = Chr+"\t"+Position+"\t"+Alt_nt+"\t"+Major+"\t"+MAF
    n+=1

m=0
for line in miss:
    if m==0:
        pass
    else:
        l = line.strip().split()
        snp2 = l[1]
        if snp2 in snpdir.keys():
            Position2 = snpdir[snp2]
            Missing = l[-1]
            if Position2 in dir.keys():
                print (dir[Position2]+"\t"+Missing)
    m+=1
        
        