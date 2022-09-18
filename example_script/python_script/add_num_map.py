# python $scripts/add_num_map.py genelocation_rangesnp.map genelocation_rangesnp_new.map 

import sys

n=0
for line in open(sys.argv[1],"r"):
    l = line.strip().split("\t")
    print ("\t".join(l[:])+"\t"+str(n))
    n+=1