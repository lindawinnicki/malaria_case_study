# Malaria_Case_Study
BINP29

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

## now we blast to find out which of our protein sequences