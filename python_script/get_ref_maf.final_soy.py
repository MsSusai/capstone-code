# python $scripts/get_ref_maf.final.py $genomefile/all.con ${i}_frq_miss.txt ${i}_haplotype.txt > ${i}_CDS_geno.txt

import sys

from Bio import SeqIO

info = sys.argv[2]
seq = sys.argv[1]
hap = sys.argv[3]

n=0
pos = []
infolist = {}
ref_base = {}
chr = ""
for line in open(info,"r"):
    if n==0:
        pass
    else:
        l = line.strip().split("\t")
        chr = l[0].capitalize()
        position = int(l[1])
        pos.append(position)
        infolist[position]="\t".join(l)
    n+=1

# print chr
# print infolist
# print pos
for line in SeqIO.parse(seq,"fasta"):
    name = line.id
    seq = line.seq
    if name[3]=="0":
        name1 = "Chr"+name[-1]
    else:
        name1 = name
    if name1 == chr:
        for i in pos:
            ref_base[i]=seq[i-1]


# print ref_base

sample_base = {}
head1 = "Chr\tPositon\tRef_nt\tAlt_nt\tMajor\tMAF\tMissing"
head = []
head.append(head1)
n=0
for j in pos:
    sample_base[j] = []
    for line in open(hap,"r"):
        l = line.strip().split(" ")
        index = l[0]
        hapseq = l[-1]
        sample_base[j].append(hapseq[n])
        if n==0:
            head.append(index)
    n+=1


print ("\t".join(head))

strings = []              
for i in pos:
    string = ""
    for k,v in sample_base.items():
        if str(k)==str(i):
            # print int(k)
            string = "\t".join(infolist[int(k)].split("\t")[0:2])+"\t"+ref_base[int(k)]+"\t"+"\t".join(infolist[int(k)].split("\t")[2:])
            for b in v:
                string+="\t"
                string+=b
            strings.append(string)

print ("\n".join(strings))


