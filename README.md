# Malaria_Case_Study
BINP29

annotating the genome for Plasmodium berghei
gmes_petap.pl --ES --min_contig 10000 --core 10 --sequence Plasmodium_berghei.genome

# filtering the avian malaria
cat Haemoproteus_tartakovskyi.raw.genome | grep -c "^>"
15048

python /resources/binp29/Data/malaria/removeScaffold.py ../../Data/Haemoproteus_tartakovskyi.raw.genome 25 filtered_Haemoproteus_tartakovskyi.genome 3000

cat filtered_Haemoproteus_tartakovskyi.genome |grep -c "^>"
1010

gmes_petap.pl --ES --min_contig 10000 --core 10 --sequence ../1_filtered/filtered_Haemoproteus_tartakovskyi.genome