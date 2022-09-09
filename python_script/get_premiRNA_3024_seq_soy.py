# python $scripts/get_miRNA_3024_seq_soy.py ${i} $pmiren/Glycine_max_basicInfo.txt $mirbase/gma.gff3 $mirbase/gma.mature.fa ${i}_haplotype.txt ${i}_frq_miss.txt ${i}_3024_seq.txt

import sys
from Bio import SeqIO

miRNAname1 = sys.argv[1]
pmiren = sys.argv[2]
mirbase = sys.argv[3]
mirbaseseq = sys.argv[4]
haplotype = sys.argv[5]
positionfile = sys.argv[6]

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
        

print(position) 

miRNAname = miRNAname1.split("_")[0]
base = miRNAname1.split("_")[1]

info = []
n=0
for line in open(pmiren,"r"):
    if n==0:
        pass
    else:
        l = line.strip().split("\t")
        name = l[0]
        if base=="PmiREN":
            if name == miRNAname:
                lll = l[4].split("-")[1]
                if lll[-2]=="0":
                    chr = "Chr"+lll[-1]
                else:
                    chr = "Chr"+lll[-2:]
                start = l[5]
                end = l[6]
                chain = l[7]
                seq = l[8]
                info.append(chr)
                info.append(start)
                info.append(end)
                info.append(chain)
                info.append(seq)
    n+=1

print(info)

mirseq = {}
for line in SeqIO.parse(mirbaseseq,"fasta"):
    id=line.id.split(" ")[0]
    seq=str(line.seq)
    seq1 = seq.replace("U","T")
    if id not in list(mirseq.keys()):
        mirseq[id] = seq1

# print mirseq

for line in open(mirbase,"r"):
    if line.startswith("#"):
        pass
    else:
        l = line.strip().split("\t")
        if l[2]=="miRNA_primary_transcript":
            anno = l[-1]
            name = anno.split(";")[2].split("=")[-1]
            if name==miRNAname:
                chr = l[0].capitalize()
                start = l[3]
                end = l[4]
                chain = l[6]
                if name in list(mirseq.keys()):
                    seq = mirseq[name]
                info.append(chr)
                info.append(start)
                info.append(end)
                info.append(chain)
                info.append(seq)
print(info)

miRNAseq = list(info[-1])
# print miRNAseq

string = []
comp_dir = {"A":"T","T":"A","G":"C","C":"G","a":"t","t":"a","a":"u","u":"a","g":"c","c":"g"}

for line in open(haplotype,"r"):
    l = line.strip().split(" ")
    sample = l[0]
    hap = l[-1]
    if info[3]=="+":
        for i in range(len(position)):
            aa = int(position[i])-int(info[1])
            if hap[i]=="-" or hap[i]=="R" or hap[i]=="S" or hap[i]=="K" or hap[i]=="M" or hap[i]=="W" or hap[i]=="Y":
                miRNAseq[aa] = major[position[i]]
            else:
                miRNAseq[aa] = hap[i]
        string.append(sample+"\t"+"".join(miRNAseq)+"\n")
    else:
        reverse = miRNAseq[::-1]
        # print reverse
        for i in range(len(reverse)):
            if reverse[i] in list(comp_dir.keys()):
                reverse[i] = comp_dir[reverse[i]]
        # print reverse
        for i in range(len(position)):
            aa = int(position[i])-int(info[1])
            # print aa
            # print position[i]
            # print hap
            # print reverse
            # print aa
            # print i
            if hap[i]=="-" or hap[i]=="R" or hap[i]=="S" or hap[i]=="K" or hap[i]=="M" or hap[i]=="W" or hap[i]=="Y":
                reverse[aa] = major[position[i]]
            else:
                reverse[aa] = hap[i]
            
        # print reverse
        reverse1 = reverse[::-1]
        # print reverse1
        for i in range(len(reverse1)):
            if reverse1[i] in list(comp_dir.keys()):
                reverse1[i] = comp_dir[reverse1[i]]
        # print reverse1
        string.append(sample+"\t"+"".join(reverse1)+"\n")

print(miRNAname+"...finished!!")
# print string
w=open(sys.argv[7],"w")
w.writelines(string)
w.close()


        
        
        
        
        
            
        
        
        
    


    