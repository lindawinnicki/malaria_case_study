#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:54:15 2026

Usage: remove_birds.py blastp_birds.txt <faa or fna> <output_name>
@author: lindawinnicki
"""

import sys

query_path = sys.argv[1]
fasta_path = sys.argv[2]
output_path = sys.argv[3]

query_list = []

with open(query_path, "r") as queries:
    for line in queries:
        if line.startswith("#"):
            continue
        query = line.partition(" ")[0] # only get the query
        query_list.append(query)


contig_list = {}

with open(fasta_path, "r") as contigs:
    for line in contigs:
        if line.startswith(">"):
            contig = line.split("\t")[2].partition("=")[2] # only get contig
            c_query = line.split("\t")[0].strip(">") # get the query
            contig_list[c_query] = contig

bird_contigs = []

for k, v in contig_list.items():
    if k in query_list:
        bird_contigs.append(v)

non_bird_contigs = {}

for k, v in contig_list.items():
    if v not in bird_contigs:
        non_bird_contigs[k] = v


# make a new file with non_bird contigs

output = ""

print_next = False # flag to print sequence too
with open(fasta_path, "r") as contigs:
    for line in contigs:
        if line.startswith(">"):
            contig = line.split("\t")[2].partition("=")[2] # only get contig
            if contig in non_bird_contigs.values():
                output += line
                print_next = True
            else:
                print_next = False
        elif print_next: # is true
            output += line

with open(output_path, "w") as nobird:
    nobird.write(output)
