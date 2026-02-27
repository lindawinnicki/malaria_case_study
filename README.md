# Malaria_Case_Study
BINP29

# annotating the genome for Plasmodium berghei

````bash
gmes_petap.pl --ES --min_contig 10000 --core 10 --sequence Plasmodium_berghei.genome
`````
# filtering the avian malaria
````bash
cat Haemoproteus_tartakovskyi.raw.genome | grep -c "^>"
````
- output: 15048

````bash
python /resources/binp29/Data/malaria/removeScaffold.py ../../Data/Haemoproteus_tartakovskyi.raw.genome 25 filtered_Haemoproteus_tartakovskyi.genome 3000
````

````bash
cat filtered_Haemoproteus_tartakovskyi.genome |grep -c "^>"
````
- output: 1010
- we filtered away 14038 sequences

# annotating the filtered data (hopefully most of them are the avian malaria protist)
````bash
gmes_petap.pl --ES --min_contig 10000 --core 10 --sequence ../1_filtered/
````
- output: filtered_Haemoproteus_tartakovskyi.genome