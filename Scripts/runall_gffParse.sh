#!/bin/bash

for file in Data/PutGenomeHere/*; do
	name=$(basename "$file") # .gtf files
	species=${name%.*} # e.g. "P_berghei" without .gft
	base=${species#P_} # e.g. berghei
	genome="Data/Plasmodium_${base}.genome"

if [[ ! -f "$genome" ]]; then
    echo "WARNING: Genome file $genome does not exist, skipping $file"
    continue
fi

if [[ $name == P_* ]]; then
	perl Scripts/gffParse.pl -c -p -g "$file" -i "$genome" -b Results/6_nobird_annotation/"$species";
fi
done