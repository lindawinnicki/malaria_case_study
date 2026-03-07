#!/bin/bash

for file in Results/10_clustal/complete_duplicated/*faa; do
name=$(basename "$file" _aligned.faa)

raxmlHPC -s "$file" -n "${name}.tre" -m PROTGAMMABLOSUM62 -p 54321 -w "/home/inf-20-2025/Malaria/Results/11_raxml/complete_duplicated" ; done