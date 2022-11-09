scripts=/home/riceUsers/zxa/soybean/scripts
refseq=/home/riceUsers/zxa/soybean/genomefile/NCBI_refseq
TF=/home/riceUsers/zxa/soybean/genomefile/phytozome
Browse=/home/riceUsers/zxa/soybean/BrowseInfo
phasidir=/home/riceUsers/zxa/soybean/genomefile/phasiRNA

# awk '$2=="lncRNA" && $1=="ncRNA"{print $0}' $refseq/GCF_000004515.5_Glycine_max_v2.1_feature_table.txt > lncRNA_table.txt
# python $scripts/get_phaseGene.fa.py lncRNA_table.txt $phasidir/phasindex.txt $refseq/GCF_000004515.5_Glycine_max_v2.1_rna.fna lncRNA.fa phasGene.fa lncANDphas.info
# python $scripts/get_TFgene.fa.py $TF/Gmax_275_Wm82.a2.v1.annotation_info.txt $TF/Gmax_275_Wm82.a2.v1.transcript.fa $Browse/browse.txt tf.fa tf.info

# cat lncRNA.fa > ncRNA.fa
# cat phasGene.fa >> ncRNA.fa
# cat tf.fa >> ncRNA.fa

# mkdir db
# makeblastdb -in ncRNA.fa -dbtype nucl -title ref -parse_seqids -out db/ncRNA

# cat lncANDphas.info > ncRNA.type.txt
# cat tf.info >> ncRNA.type.txt
# python $scripts/blast_type.sql.py ncRNA.type.txt



#根据Browse结果提fasta和info
python $scripts/get_blast_info.py $Browse/all_information_final.txt $refseq/GCF_000004515.5_Glycine_max_v2.1_rna.fna $TF/Gmax_275_Wm82.a2.v1.transcript.fa ncRNA_new.fa ncRNA_type.info
python $scripts/get_blast_info_codinggene.py $Browse/codinggene_information_updata.txt $TF/Gmax_275_Wm82.a2.v1.transcript.fa codinggene_new.fa codinggene_type.info

mkdir db
makeblastdb -in ncRNA_new.fa -dbtype nucl -title ref -parse_seqids -out db/ncRNA
makeblastdb -in codinggene_new.fa -dbtype nucl -title ref -parse_seqids -out db/codinggene

awk -F "\t" 'NR>1{print ">"$1"\n"$5}' $Browse/phasiRNA_information_new.txt > phasiRNA.fa
awk -F "\t" '{print ">"$1"_"$2"\n"$3}' $Browse/miRNA_information_new.txt > miRNA.fa

awk -F "\t" 'NR>1{print $1"\t"$7"\t"$2"\tphasiRNA"}' $Browse/phasiRNA_information_new.txt >phasiRNA_type.info
awk -F "\t" '{print $1"\t"$2"\tmiRNA"}' $Browse/miRNA_information_new.txt > miRNA_type.info

cp phasiRNA.fa sRNA.fa
cat miRNA.fa >> sRNA.fa

#去重
cat sRNA.fa | paste - - | sort | uniq | awk '{print $1"\n"$2}' > sRNA_new.fa
makeblastdb -in sRNA_new.fa -dbtype nucl -title ref -parse_seqids -out db/sRNA

#将fasta序列换成id \tab seq 传入数据库
python $scripts/get_blast_seq.py ncRNA_new.fa ncRNA_blast_seq.txt
python $scripts/get_blast_seq.py codinggene_new.fa codinggene_blast_seq.txt

python $scripts/blast_type.sql.py ncRNA_type.info ncRNA
python $scripts/blast_type.presql.py ncRNA_type.info ncRNA
python $scripts/blast_type.sql.py phasiRNA_type.info phasiRNA 
python $scripts/blast_type.presql.py phasiRNA_type.info phasiRNA 
python $scripts/blast_type.sql.py miRNA_type.info miRNA
python $scripts/blast_type.presql.py miRNA_type.info miRNA
python $scripts/blast_type.sql.py codinggene_type.info codinggene
python $scripts/blast_type.presql.py codinggene_type.info codinggene
python $scripts/blast_seq.presql.py ncRNA_blast_seq.txt ncRNA
python $scripts/blast_seq.presql.py codinggene_blast_seq.txt coding

makeblastdb -in ../genomefile/Gmax_275_Wm82.a2.v1.cds.fa -dbtype nucl -title ref -parse_seqids -out db/cds