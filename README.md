# Malaria_Case_Study
## Versions
 - Protein-Protein BLAST 2.11.0+
 - GeneMark-ES Suite version 4.* (2021)
 - gffParse.pl version 1.1


# Workflow
#### annotating the genome (Plasmodium berghei)
````bash
gmes_petap.pl --ES # eukaroyitc self training 
--min_contig 10000 # min contig length for unsupervised learning
--core 10 
--sequence Plasmodium_berghei.genome
````
- copy the rest annotated from server

## filtering the avian malaria (Haemoproteus tartakovskyi)
````bash
cat Haemoproteus_tartakovskyi.raw.genome | grep -c "^>"
````
- \# of contigs = 15048

### run script from server
- remove contigs >25% GC-content
- only keep contigs >3000bp
````bash
python /resources/binp29/Data/malaria/removeScaffold.py \\
../../Data/Haemoproteus_tartakovskyi.raw.genome 25 \\
filtered_Haemoproteus_tartakovskyi.genome 3000
````
````bash
cat filtered_Haemoproteus_tartakovskyi.genome | grep -c "^>"
````
- output: 1010
-- we filtered away 14038 sequences

### annotating the filtered data (hopefully most of them are the avian malaria protist)
````bash
gmes_petap.pl --ES  # eukaroyitc self training 
--min_contig 10000 # min contig length for unsupervised learning
--core 10 
--sequence ../1_filtered/
````
- output: filtered_Haemoproteus_tartakovskyi.genome

### clean up the gtf file for avian malaria
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
- beacuse right now it has extra cols: "GC", "length"
````bash
cat Haemoproteus_tartakovskyi.gtf \\
| sed "s/ GC.*\tGeneMark.hmm/\tGenemark.hmm/" \\
> filtered_Haemoproteus_tartakovskyi.gtf
````

### .fna and .faa files from gtf (fasta)
````bash
perl ../../Scripts/gffParse.pl # version 1.1
-c # find the most probable reading frame
-p # amino acid
-g ../2_annotation/filtered_Haemoproteus_tartakovskyi.gtf 
-i ../1_filtered/filtered_Haemoproteus_tartakovskyi.genome # fasta
````

## BLAST to find out which of our protein sequences remain to be avian
````bash
# Protein-Protein BLAST 2.11.0+
blastp -query 3_fasta/gffParse.faa 
-db SwissProt \\
-num_descriptions 10 \\
-out 4_blastp/Haemoproteus_tartakovskyi.blastp \\
-num_threads 10 \\
-num_alignments 10

# Translated Query-Protein Subject BLAST 2.11.0+
blastx -query 3_fasta/gffParse.fna \\
-db SwissProt \\
-num_descriptions 10 \\
-out 4_blastp/Haemoproteus_tartakovskyi.blastx \\
-num_threads 10 \\
-num_alignments 10
````

### i made a table out of the results
```bash
# blastx
python lindawinnicki_blastParser_SwissProt.py Haemoproteus_tartakovskyi.blastx blastx_table.txt
# blastp
python lindawinnicki_blastParser_SwissProt.py Haemoproteus_tartakovskyi.blastp blastp_table.txt
```
output:
- blastp_table.txt
- blastx_table.txt

### python script that outputs out all bird matches
when browsing through the blast results ([https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/docs/speclist.txt]), a very broad phylogenetic range could be matched. this could propose very conserved regions. therefor, the sequences were instead browsed for our specific host (siskin bird). no matches were found here neither, so i stepped down the tree to 'birds (Aves)' and found out those matches:
````bashgit status
python swissProtUniProt.py # input should be changed in script (blastp/blastx_table.txt)
````
filtered for e-value<0.05
````bash
awk '$4 < 0.05' blast_birds.txt > blast_birds_005.txt
````
#### making important files unwritable
````bash
chmod -w blast_birds_005.txt \\ # make unwritable
    ../Results/3_fasta/gffParse.faa \\
    ../Results/3_fasta/gffParse.fna \\
    ../Results/4_blastp/blast_birds_005.txt \\
    ../Results/4_blastp/Haemoproteus_tartakovskyi_blastp_results.txt \\
    ../Results/4_blastp/Haemoproteus_tartakovskyi_blastx_result.txt
````

### run python script to remove bird matches
, though i am not sure if really needed. Creates faa and fna.

\# contigs removed = 173

\# contigs remaining = 1263
````bash
 python3 remove_birds.py blast_birds_005.txt ../Results/3_fasta/gffParse.faa ../Results/3_fasta/no_bird.faa # amino acid
 
 python3 remove_birds.py blast_birds_005.txt ../Results/3_fasta/gffParse.fna ../Results/3_fasta/no_bird.fna # DNA
 ````

 ### add output directory within "Scripts" to tidy up
 ````bash
 ~/Malaria/Scripts $ mkdir output
 mv blast* output/
 ````

## filling out the table
````bash
cat P_berghei.gtf | grep -v "^#"| cut -f3 | sort | uniq -c # genes


# calculate GC:
cat Plasmodium_berghei.genome | grep -v "^>" | tr -d "\n" | wc -c # genome size
cat Plasmodium_berghei.genome | grep -v "^>" | tr -d "\nATN" | wc -c # gc basepairs
awk ' BEGIN {print 4257744/17954629} '
0.237139

````


| Species    | Host | Genome size | Genes | Genomic GC |
| -------- | ------- | -------- | ------- | -------- |
|Plasmodium berghei|rodents|17954629|7235|23.7%
|Plasmodium cynomolgi|macaques|26181343|5787|39.1%
|Plasmodium falciparum|humans|23270305|5207|19.4%
|Plasmodium knowlesi|lemures|23462346|4953|37.5%
|Plasmodium vivax|humans|27007701|5682|42.2%
|Plasmodium yoelii|rodents|22222369|4919|20.8%
|Haemoproteus tartakovskyi|birds|6265874|1437|23.6%
|Toxoplasma gondii|humans|128105889bp||52.5%


#### run gene prediction again (done to be used for creating a phylogenetic tree)
------stop
### at this time point i realise that i have accidently screwed up my blast searches, where ive used fna with blastp and faa with blastx. so i am rerunning things, and i have corrected this readmefile. and now I realise that the xscript removing bird contigs should have been doing that on the filtered genome file....