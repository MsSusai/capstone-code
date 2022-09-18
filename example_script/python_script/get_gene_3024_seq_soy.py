	# python $scripts/get_gene_3024_seq_soy.py ${j} $i.range.pos $genomefile/Gmax_275_v2.0.fa ${j}_haplotype.txt ${j}_frq_miss.txt ${j}_3024_seq.txt

import sys
from Bio import SeqIO

genename = sys.argv[1]
gff3 = sys.argv[2]
genomseq = sys.argv[3]
haplotype = sys.argv[4]
positionfile = sys.argv[5]

position = []
n=0
major = {}
for line in open(positionfile,"r"):
    if n==0:
        pass
    else:
        l = line.strip().split("\t")
        position.append(l[1])
        major[l[1]] = l[3]
    n+=1


print position 


# print genename

chrID2 = ""
info = []
for line in open(gff3,"r"):
    l = line.strip().split("\t")
    name = l[-1]
    if name==genename:
        chrID2=l[2].capitalize()
        start = l[3]
        end = l[4]
        chain = l[6]
        info.append(start)
        info.append(end)
        info.append(chain)
        break

print chrID2
print info

lncseq = []
for line in SeqIO.parse(genomseq,"fasta"):
    id=line.id.split(" ")[0]
    if id==chrID2:
        seq=str(line.seq)
        start = int(info[0])
        end = int(info[1])+1
        lncseq = list(seq[start:end].upper())

# print lncseq
print len(lncseq)


string = []
comp_dir = {"A":"T","T":"A","G":"C","C":"G","a":"t","t":"a","g":"c","c":"g"}

for line in open(haplotype,"r"):
    l = line.strip().split(" ")
    sample = l[0]
    hap = l[-1]
    if info[2]=="+":
        for i in range(len(position)):
            aa = int(position[i])-int(info[0])
            if hap[i]=="-" or hap[i]=="R" or hap[i]=="S" or hap[i]=="K" or hap[i]=="M" or hap[i]=="W" or hap[i]=="Y":
                lncseq[aa] = major[position[i]]
            else:
                lncseq[aa] = hap[i]
        string.append(sample+"\t"+"".join(lncseq)+"\n")
    else:
        reverse = lncseq[::-1]
        # print reverse
        for i in range(len(reverse)):
            if reverse[i] in comp_dir.keys():
                reverse[i] = comp_dir[reverse[i]]
        # print reverse
        for i in range(len(position)):
            aa = int(position[i])-int(info[0])
            # print aa
            # print position[i]
            # print hap
            # print reverse
            # print i
            if hap[i]=="-" or hap[i]=="R" or hap[i]=="S" or hap[i]=="K" or hap[i]=="M" or hap[i]=="W" or hap[i]=="Y":
                reverse[aa] = major[position[i]]
            else:
                reverse[aa] = hap[i]
            
        # print reverse
        reverse1 = reverse[::-1]
        # print reverse1
        for i in range(len(reverse1)):
            if reverse1[i] in comp_dir.keys():
                reverse1[i] = comp_dir[reverse1[i]]
        # print reverse1
        string.append(sample+"\t"+"".join(reverse1)+"\n")

print genename+"...finished!!"
# print string
w=open(sys.argv[6],"w")
w.writelines(string)
w.close()


        
        
        
        
        
            
        
        
        
    


    