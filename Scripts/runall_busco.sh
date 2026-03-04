#!/bin/bash

for file in Results/6_nobird_annotation/*.faa; do
	name=$(basename "$file") # .faa files
	species=${name%.*} # e.g. "P_berghei" without .faa

	busco \
	-i "$file" \
	-o Results/8_busco/"$species" \
	-m prot \
	-l apicomplexa \
	--cpu 10
done