# Malaria_Case_Study
BINP29
 - Protein-Protein BLAST 2.11.0+

## annotating the genome for Plasmodium berghei

````bash
gmes_petap.pl --ES --min_contig 10000 --core 10 --sequence Plasmodium_berghei.genome
````

# filtering the avian malaria

````bash
cat Haemoproteus_tartakovskyi.raw.genome | grep -c "^>"
````
- output: 15048

````bash
python /resources/binp29/Data/malaria/removeScaffold.py ../../Data/Haemoproteus_tartakovskyi.raw.genome 25 filtered_Haemoproteus_tartakovskyi.genome 3000
````

````bash
cat filtered_Haemoproteus_tartakovskyi.genome | grep -c "^>"
````
- output: 1010
- we filtered away 14038 sequences

## annotating the filtered data (hopefully most of them are the avian malaria protist)

````bash
gmes_petap.pl --ES --min_contig 10000 --core 10 --sequence ../1_filtered/
````

- output: filtered_Haemoproteus_tartakovskyi.genome

## clean up the gtf file for avian malaria
we want to clean the gtf file, so it fits in this template:
````bash
# 0 seqname
# 1 source
# 2 feature
# 3 start
# 4 end
# 5 score
# 6 strand
# 7 phase
# 8 [attributes]
# 9 [comments]
````
- beacuse right now it has extra cols: GC, length
````bash
cat Haemoproteus_tartakovskyi.gtf | sed "s/ GC.*\tGeneMark.hmm/\tGenemark.hmm/" > clean_Haemoproteus_tartakovskyi.gtf
````
## get fasta and protein sequence files from gtf
````bash
perl ../../Scripts/gffParse.pl -c -p -g ../2_annotation/clean_Haemop
roteus_tartakovskyi.gtf -i ../1_filtered/filtered_Haemoproteus_tartakovskyi.genome 
````

## now we blast to find out which of our protein sequences remain to be avian
````bash
# Protein-Protein BLAST 2.11.0+
blastp -query 3_fasta/gffParse.fna -db SwissProt -num_descriptions 10 -out 4_blastp/Haemoproteus_tartakovskyi.blastp -num_threads 10 -num_alignments 10

# Translated Query-Protein Subject BLAST 2.11.0+
blastx -query 3_fasta/gffParse.faa -db SwissProt -num_descriptions 10 -out 4_blastp/Haemoproteus_tartakovskyi.blastx -num_threads 10 -num_alignments 10
````

## i made a table out of the results
```bash
# blastx
python lindawinnicki_blastParser_SwissProt.py Haemoproteus_tartakovskyi.blastx blastx_table.txt
# blastp
python lindawinnicki_blastParser_SwissProt.py Haemoproteus_tartakovskyi.blastp blastp_table.txt
```

output:
- blastp_table.txt
- blastx_table.txt

## we use a python script that finds out all different bird matches
when browsing through the blast results ([https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/docs/speclist.txt]), a very broad phylogenetic range could be matched. this could propose very conserved regions. therefor, the sequences were instead browsed for our specific host (siskin bird). no matches were found here neither, so i stepped down the tree to 'birds (Aves)' and found out those matches:

````bash
python swissProtUniProt.py # input should be changed in script (blastp/blastx_table.txt)
````
all matches where then filtered for a lower e value than 0.05
````bash
awk '$4 < 0.05' blast_birds.txt > blast_birds_005.txt
chmod -w blast_birds_005.txt \\ # make unwritable
    ../Results/3_fasta/gffParse.faa \\
    ../Results/3_fasta/gffParse.fna \\
    ../Results/4_blastp/blastp_table.txt \\
    ../Results/4_blastp/blastx_table.txt \\
    ../Results/4_blastp/Haemoproteus_tartakovskyi_blastp_results.txt \\
    ../Results/4_blastp/Haemoproteus_tartakovskyi_blastx_result.txt
````

run script to remove bird matches
````bash
 python3 remove_birds.py blast_birds_005.txt ../Results/3_fasta/gffParse.faa ../Results/3_fasta/no_bird.faa # amino acid

  python3 remove_birds.py blast_birds_005.txt ../Results/3_fasta/gffParse.fna ../Results/3_fasta/no_bird.fna # DNA
 ````