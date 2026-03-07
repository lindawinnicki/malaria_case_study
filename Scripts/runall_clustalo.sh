#!/bin/bash

for file in Results/9_busco_fastas/complete_duplicated/*faa; do
name=$(basename "$file" .faa)

clustalo -i "$file" -o "Results/10_clustal/${name}_aligned.faa" -v ; done