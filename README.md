# Malaria_Case_Study

# working tree
````bash
.
├── busco_downloads
│   ├── file_versions.tsv
│   └── lineages
│       └── apicomplexa_odb12
│           ├── ancestral
│           ├── ...
├── Data
│   ├── Gmes
│   │   ├── data
│   │   │   ├── dna.fna 
│   │   │   ├── ...
│   │   ├── ...
│   ├── Haemoproteus_tartakovskyi.raw.genome
│   ├── Plasmodium_berghei.genome
│   ├── Plasmodium_cynomolgi.genome
│   ├── Plasmodium_faciparum.genome
│   ├── plasmodiumGenomes.tgz
│   ├── Plasmodium_knowlesi.genome
│   ├── Plasmodium_vivax.genome
│   ├── Plasmodium_yoelii.genome
│   ├── PutGenomeHere
│   │   ├── P_berghei.gtf
│   │   ├── P_cynomolgi.gtf
│   │   ├── P_falciparum.gtf
│   │   ├── P_knowlesi.gtf
│   │   ├── P_vivax.gtf
│   │   ├── P_yoelii.gtf
│   │   └── Tg.gff
│   └── Toxoplasma_gondii.genome
├── Docs
│   ├── answers.md
│   └── plasmodiumGenomes.txt
├── README.md
├── Results
│   ├── 1_filtered
│   │   └── filtered_Haemoproteus_tartakovskyi.genome
│   ├── 2_annotation
│   │   ├── clean_Haemoproteus_tartakovskyi.gtf
│   │   ├── Gmes
│   │   │   ├── data
│   │   │   ├── ...
│   │   └── Haemoproteus_tartakovskyi.gtf
│   ├── 3_fasta
│   │   ├── gffParse.faa
│   │   ├── gffParse.fna
│   │   ├── no_bird.faa
│   │   └── no_bird.fna
│   ├── 4_blastp
│   │   ├── bad_blast
│   │   │   ├── blastp_table.txt
│   │   │   ├── blastx_table.txt
│   │   │   ├── Haemoproteus_tartakovskyi_blastp_results.txt
│   │   │   └── Haemoproteus_tartakovskyi_blastx_result.txt
│   │   ├── blast_job.out
│   │   ├── faa_Haemoproteus_tartakovskyi.blastp
│   │   ├── fna_Haemoproteus_tartakovskyi.blastx
│   │   └── nohup.out
│   ├── 5_nobird_genome
│   │   ├── gmes_output
│   │   │   ├── data
│   │   │   ├── genemark.gtf
│   │   │   ├── gmes.log
│   │   │   ├── gmhmm.mod
│   │   │   ├── info
│   │   │   ├── output
│   │   │   ├── run
│   │   │   └── run.cfg
│   │   └── no_bird.genome
│   ├── 6_nobird_annotation
│   │   ├── H_tartakovskyi.faa
│   │   ├── H_tartakovskyi.fna
│   │   ├── H_tartakovskyi.log
│   │   ├── myproject.blast-graph
│   │   ├── myproject.info
│   │   ├── myproject.proteinortho-graph
│   │   ├── myproject.proteinortho-graph.summary
│   │   ├── myproject.proteinortho.html
│   │   ├── myproject.proteinortho.tsv
│   │   ├── nohup.out
│   │   ├── P_berghei.faa
│   │   ├── P_berghei.fna
│   │   ├── P_berghei.log
│   │   ├── P_cynomolgi.faa
│   │   ├── P_cynomolgi.fna
│   │   ├── P_cynomolgi.log
│   │   ├── P_faciparum.faa
│   │   ├── P_faciparum.fna
│   │   ├── P_faciparum.log
│   │   ├── P_knowlesi.faa
│   │   ├── P_knowlesi.fna
│   │   ├── P_knowlesi.log
│   │   ├── P_vivax.faa
│   │   ├── P_vivax.fna
│   │   ├── P_vivax.log
│   │   ├── P_yoelii.faa
│   │   ├── P_yoelii.fna
│   │   ├── P_yoelii.log
│   │   ├── T_gondii.faa
│   │   ├── T_gondii.fna
│   │   └── T_gondii.log
│   ├── 7_proteinortho
│   │   ├── H_tartakovskyi.faa.diamond.dmnd
│   │   ├── H_tartakovskyi.faa.len
│   │   ├── myproject.blast-graph
│   │   ├── myproject.info
│   │   ├── myproject.proteinortho-graph
│   │   ├── myproject.proteinortho-graph.summary
│   │   ├── myproject.proteinortho.html
│   │   ├── myproject.proteinortho.tsv
│   │   ├── nohup.out
│   │   ├── P_berghei.faa.diamond.dmnd
│   │   ├── P_berghei.faa.len
│   │   ├── P_cynomolgi.faa.diamond.dmnd
│   │   ├── P_cynomolgi.faa.len
│   │   ├── P_faciparum.faa.diamond.dmnd
│   │   ├── P_faciparum.faa.len
│   │   ├── P_knowlesi.faa.diamond.dmnd
│   │   ├── P_knowlesi.faa.len
│   │   ├── P_vivax.faa.diamond.dmnd
│   │   ├── P_vivax.faa.len
│   │   ├── P_yoelii.faa.diamond.dmnd
│   │   ├── P_yoelii.faa.len
│   │   ├── T_gondii.faa.diamond.dmnd
│   │   └── T_gondii.faa.len
│   ├── 8_busco
│   │   ├── H_tartakovskyi
│   │   │   ├── logs
│   │   │   │   ├── busco.log
│   │   │   │   ├── hmmsearch_err.log
│   │   │   │   └── hmmsearch_out.log
│   │   │   ├── run_apicomplexa_odb12
│   │   │   │   ├── busco_sequences
│   │   │   │   │   ├── fragmented_busco_sequences
│   │   │   │   │   │   ├── 11416at5794.faa
│   │   │   │   │   │   ├── ..
│   │   │   │   │   ├── multi_copy_busco_sequences
│   │   │   │   │   └── single_copy_busco_sequences
│   │   │   │   │       ├── 10285at5794.faa
│   │   │   │   │       ├── ...
│   │   │   │   ├── full_table.tsv
│   │   │   │   ├── hmmer_output
│   │   │   │   │   ├── initial_run_results
│   │   │   │   │   │   ├── 10182at5794.out
│   │   │   │   │   │   ├── ...
│   │   │   │   │   └── rerun_results
│   │   │   │   ├── missing_busco_list.tsv
│   │   │   │   ├── short_summary.json
│   │   │   │   └── short_summary.txt
│   │   │   ├── short_summary.specific.apicomplexa_odb12.H_tartakovskyi.json
│   │   │   └── short_summary.specific.apicomplexa_odb12.H_tartakovskyi.txt
│   │   ├── P_berghei
│   │   │   ├── logs
│   │   │   └── ...
│   │   ├── P_cynomolgi
│   │   │   ├── logs
│   │   │   └── ...
│   │   ├── P_faciparum
│   │   │   ├── logs
│   │   │   └── ...
│   │   ├── P_knowlesi
│   │   │   ├── logs
│   │   │   └── ...
│   │   ├── P_vivax
│   │   │   ├── logs
│   │   │   └── ...
│   │   ├── P_yoelii
│   │   │   ├── logs
│   │   │   └── ...
│   │   └── T_gondii
│   │   │   ├── logs
│   │   │   └── ...
│   ├── 9_busco_fastas
│   │   ├── complete_duplicated
│   │   │   ├── 10954at5794.faa
│   │   │   ├── ...
│   │   └── complete_only
│   │      ├── 10954at5794.faa
│   │   
│   ├──  10_clustal
│   │   ├── complete_duplicated
│   │   │   ├── 10954at5794_aligned.faa
│   │   │   └── ...
│   │   └── complete_only
│   │       ├── 10954at5794_aligned.faa
│   │       ├── 68804at5794_aligned.faa.reduced
│   │       ├── ...
│   ├── 11_raxml
│   │   ├── complete_duplicated
│   │   │   ├── all_best.tre
│   │   │   ├── RAxML_bestTree.10954at5794.tre
│   │   │   ├── RAxML_info.10954at5794.tre
│   │   │   ├── RAxML_log.9722at5794.tre
│   │   │   ├── RAxML_parsimonyTree.11330at5794.tre
│   │   │   ├── RAxML_result.10954at5794.tre
│   │   │   ├── ...
│   │   └── complete_only
│   │       ├── all_best.tre
│   │       ├── RAxML_bestTree.10954at5794.tre
│   │       ├── RAxML_info.9722at5794.tre
│   │       ├── RAxML_log.10954at5794.tre
│   │       ├── RAxML_parsimonyTree.10954at5794.tre
│   │       ├── RAxML_result.10954at5794.tre
│   │       ├── ...
│   └── 12_consensus
│   │   ├── complete_duplicated
│   │   │   ├── outfile
│   │   │   └── outtree
│   │   └── complete_only
│   │       ├── outfile
│   │       ├── outtree
│   │       ├── root_outfile
│   │       └── root_outtree
│           ├── ...

├── Scripts
│   ├── bad_output
│   │   ├── blastp_table.txt
│   │   ├── blastp_unique.txt
│   │   ├── blastx_table.txt
│   │   ├── blastx_unique.txt
│   │   └── remove_birds.py
│   ├── busco_to_fasta.py
│   ├── filtered_copy.genome
│   ├── gffParse.pl
│   ├── gmes_petap.pl
│   ├── lindawinnicki_blastParser_SwissProt.py
│   ├── new_removebirds.py
│   ├── output
│   │   ├── blast_birds_005.txt
│   │   ├── blast_birds.txt
│   │   ├── new_blastp_table.txt
│   │   └── new_blastx_table.txt
│   ├── removeScaffold_copy.py
│   ├── removeScaffold.py
│   ├── runall_busco.sh
│   ├── runall_clustalo.sh
│   ├── runall_gffParse.sh
│   ├── runall_raxml.sh
│   ├── swissProtUniProt.py
│   └── tmp.txt
└── tre.txt

167 directories, 26366 files
````

## Versions
 - Protein-Protein BLAST 2.11.0+
 - GeneMark-ES Suite version 4.* (2021)
 - gffParse.pl version 1.1
 - Proteinortho with PoFF version 6.3.6 - An orthology detection tool
 - BUSCO 6.0.0
 - clustalo Clustal Omega - 1.2.4
 - RAxML version 8.2.12 May 2018.


# Workflow
#### annotating the genome (Plasmodium berghei)
````bash
gmes_petap.pl --ES # eukaroyitc self training 
--min_contig 10000 # min contig length for unsupervised learning
--core 10 
--sequence Plasmodium_berghei.genome
````
- copy the rest annotated from server

## 1. filtering the avian malaria (Haemoproteus tartakovskyi)
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

## 2. annotating the filtered data (hopefully most of them are the avian malaria protist)
````bash
:~Malaria/Results$ mkdir 2_annotation # new dir
cd 2_annotation

gmes_petap.pl --ES  # eukaroyitc self training 
--min_contig 10000 # min contig length for unsupervised learning
--core 10 
--sequence ../1_filtered/filtered_Haemoproteus_tartakovskyi.genome
````
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

## 3. get protein files (.fna and .faa)
````bash
perl ../../Scripts/gffParse.pl # version 1.1
-c # find the most probable reading frame
-p # amino acid
-g ../2_annotation/filtered_Haemoproteus_tartakovskyi.gtf 
-i ../1_filtered/filtered_Haemoproteus_tartakovskyi.genome # fasta
-b Haemoproteus_tartakovskyi
````

## 4. BLAST to find out which of our protein sequences remain to be avian
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

## !!! 5. python script that outputs out all bird matches
when browsing through the blast results ([https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/docs/speclist.txt]), a very broad phylogenetic range could be matched. this could propose very conserved regions. therefor, the sequences were instead browsed for our specific host (siskin bird). no matches were found here neither, so i stepped down the tree to 'birds (Aves)' and found out those matches:
````bash
python swissProtUniProt.py # input should be changed in script (blastp/blastx_table.txt)
````
filtered for e-value<0.05
````bash
awk '$4 < 0.05' blast_birds.txt > blast_birds_005.txt
````
### making important files unwritable
````bash
chmod -w blast_birds_005.txt \\ # make unwritable
    ../Results/3_fasta/gffParse.faa \\
    ../Results/3_fasta/gffParse.fna \\
    ../Results/4_blastp/blast_birds_005.txt \\
    ../Results/4_blastp/Haemoproteus_tartakovskyi_blastp_results.txt \\
    ../Results/4_blastp/Haemoproteus_tartakovskyi_blastx_result.txt
````
# --- stop and jump to actual 5 from here. 
### run python script to remove bird matches
, though i am not sure if really needed. Creates faa and fna.

````bash
 python3 remove_birds.py blast_birds_005.txt ../Results/3_fasta/gffParse.faa ../Results/3_fasta/no_bird.faa # amino acid
 
 python3 remove_birds.py blast_birds_005.txt ../Results/3_fasta/gffParse.fna ../Results/3_fasta/no_bird.fna # DNA
 ````
 - \# contigs removed = 173

 - \# contigs remaining = 1263

 ### add output directory within "Scripts" to tidy up
 ````bash
 ~/Malaria/Scripts $ mkdir output
 mv blast* output/
 ````

# ------continue 
### at this time point i realise that i have accidently screwed up my blast searches, where ive used fna with blastp and faa with blastx. so i am rerunning things, and i have corrected this readmefile. 
### and I realise that the script removing bird contigs should have been doing that on the filtered genome file....

## actual 5. filter the genome from bird-matching contigs
````bash
python new_removebirds.py \\
output/blast_birds_005.txt \\ # queries
../Results/3_fasta/gffParse.fna \\ # match queries w contig
../Results/1_filtered/filtered_Haemoproteus_tartakovskyi.genome \\ # genome fasta
../Results/5_nobird_genome/no_bird.genome # output
````
- output: no_bird.genome
````bash
grep "^>" no_bird.genome | wc -l
chmod -w no_bird.genome # make unreadable
````
- output: 
- removed 86 sequences 
- 924 remaining sequences

#### annotate the newly filtered genome again
````bash
mkdir 6_nobird_annotation # new directory
cd 6_nobird_annotation/

gmes_petap.pl --ES  # eukaroyitc self training 
--min_contig 10000 # min contig length for unsupervised learning
--core 10 
--sequence ../5_nobird_genome/no_bird.genome
````

# filling out the table
````bash
cat P_berghei.gtf | grep -v "^#"| cut -f3 | sort | uniq -c # genes

cat Tg.gff | cut -f9 | tail # toxoplasma genes are sorted numerically by "gene_id"

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
|Toxoplasma gondii|humans|128105889bp|15892|52.5%
## 6. run gene prediction again (to be used for creating a phylogenetic tree)
#### this is done because the genemark is training on what feed into it. if we have bird + malaria scaffold, the predicition will be somewhere in between. 
### protein and nuclear files
````bash
perl Scripts/gffParse.pl \\
-c \\
-p \\
-g Data/PutGenomeHere/Tg.gff \\
-i Data/Toxoplasma_gondii.genome \\
-b Results/6_nobird_annotation/T_gondii

perl Scripts/gffParse.pl \\
-c \\
-p \\
-g Results/2_annotation/clean_Haemoproteus_tartakovskyi.gtf \\
-i Results/5_nobird_genome/no_bird.genome \\
-b Results/6_nobird_annotation/H_tartakovskyi

bash Scripts/runall_gffParse.sh

cd Results/6_nobird_annotation
chmod -w *.faa
````
## proteinortho
````bash
conda create -n proteinortho # env
conda activate proteinortho #version 6.3.6
conda install bioconda::proteinortho

:~/Malaria/Results$ mkdir 7_proteinortho
cd 7_proteinortho

# proteinortho requested to run the following:
for f in *.faa; do
    sed -i -E '/^>/! s/[^XOUBZACDEFGHIKLMNPQRSTVWYxoubzacdefghiklmnpqrstvwy]//g; /^$/d' "$f"
done
# then run this:
nohup proteinortho6.pl \\ # version 6.3.6
../6_nobird_annotation/*.faa -project=myproject &
````
## 7.  busco all 
````bash
conda create -n busco
conda activate busco
conda install bioconda::busco # BUSCO 6.0.0

:~/Malaria/Results$ mkdir 8_busco # new dir

bash Scripts/runall_busco.sh
````


## 8. gather all orthologs
````bash
chmod -R a-w Results/8_busco/ # protect the files

python Scripts/busco_to_fasta.py 
````

## 9. cluster
````bash
:~/Malaria/Results$ mkdir 10_clustal

nohup bash Scripts/runall_clustalo.sh &
````

````bash
:~/Malaria/Results$ mkdir 11_raxml

nohup bash Scripts/runall_raxml.sh
````

## 10. consensus tree
````bash
conda create -n phylip
conda activate phylip
conda install bioconda::phylip

cd Results/11_raxml
cat RAxML_bestTree.* > all_best.tre

:~/Malaria/Results$ mkdir 12_consensus
cd 12_consensus
consense # version 3.697
# Please enter a new file name> ../11_raxml/all_best.tre
````


# cleaning up the working directory and redoing 8-10 for complete AND duplicates (modified python script - "busco_to_fasta")
````bash
:~/Malaria/Results/9_busco_fastas$ mkdir complete_only complete_duplicated
mv *.faa complete_only/ #from 8_busco_fastas

:~/Malaria/Results/10_clustal$ mkdir complete_only complete_duplicated
mv * complete_only/ # from 10_clustal

:~/Malaria/Results/11_raxml$ mkdir complete_only complete_duplicated
mv *.tre complete_only/ # from 11_raxml

:~/Malaria/Results/12_consensus$ mkdir complete_only complete_duplicated # from 12_consensus
mv *e complete_only/


# busco to fasta (both complete and 1 of each duplicate)
python Scripts/busco_to_fasta.py 

# clustalo
conda activate alignment # activate env
chmod -w *.faa
nohup bash Scripts/runall_clustalo.sh &

# raxml
nohup bash Scripts/runall_raxml.sh %
cat RAxML_bestTree.* > all_best.tre
chmod -w *.tre

# consense
consense
# Please enter a new file name> Results/11_raxml/complete_duplicated/all_best.tre
````

````bash
Extended majority rule consensus tree

CONSENSUS TREE:
the numbers on the branches indicate the number
of times the partition of the species into the two sets
which are separated by that branch occurred
among the trees, out of  53.00 trees

                                          +-------P yoelii
                          +----------49.0-|
                          |               +-------P berghei
                  +--16.0-|
                  |       |       +---------------P knowlesi
                  |       +--40.0-|
          +--37.0-|               |       +-------P cynomolgi
          |       |               +--36.0-|
          |       |                       +-------P vivax
  +-------|       |
  |       |       +-------------------------------P faciparum
  |       |
  |       +---------------------------------------H tartakovskyi
  |
  +-----------------------------------------------T gondii



````