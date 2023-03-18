ls *.out > out_list.txt
for a in `cat out_list.txt`;do

cat $a|grep '^sp|'|awk -F ' '   '{print $1}' |awk -F '|'   '{print $2,$3}'  >> out.txt
cat test.out|grep '^sp|'|awk -F '  ' '{print $2}'  >>bitscore.txt
cat test.out|grep '^sp|'|awk -F ' ' '{print $NF}'  >> E_value.txt

grep 'Identities' $a|awk '{print($3,$4)}' >> tem.txt
# awk 'BEGIN {print} {print $0}' tem.txt  >> temp.txt
paste   out.txt tem.txt  bitscore.txt E_value.txt >> out_result.txt
echo >> out_result.txt
sed -i -e '/>sp/d' out_result.txt
sed -i 's/\t/ /g' out_result.txt
sed -i 's/,/ /g' out_result.txt

rm out_list.txt tem.txt  out.txt  bitscore.txt E_value.txt 

echo "Input file:"  $a >> Blast_result.txt
cat $a|grep 'Query=' >> Blast_result.txt
echo '-------------------------------'>> Blast_result.txt
echo 'ID Entry_Name Identities Bits-Score E_Value'>> Blast_result.txt
cat  out_result.txt >> Blast_result.txt

rm  out_result.txt
done