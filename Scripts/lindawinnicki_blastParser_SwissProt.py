#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

blastParser.py

A script that reformats .blastp to .txt with tab-delimiters, with columns containing:
    Query, Protein-hit, e-value, identity precentage and score (bits).

------------------

Input: .blastp file

Output: text file, e.g. .txt, .tsv. Specify in command line!

------------------

Usage:
    python lindawinnicki_blastParser.py input.blastp output.txt

------------------
python 3.12.11
27th Jan 2025
Linda Winnicki
"""
#%%
import sys

# try: 
#     if len(sys.argv) < 3 or len(sys.argv) > 4:
#         raise Exception("\nMake sure you wrote the arguments correctly!\n"
#                         "'python lindawinnicki_blastParser.py input.blastp output.txt'\n")
# except Exception as arg_message:
#     print(arg_message)
# #     sys.exit()

# path_blast = sys.argv[1]
# path_output = sys.argv[2]
#%%

########tmp
path_blast="tmp.blastp"
path_output="tmp_result.txt"

"""
--------------------------------------------- Reading Blast File --------------------------------------------

While reading the blastp file, create variables for all the wanted columns within a 'for loop'. The partitioning method is widely used here to separate specific statistics/words from line patterns in the file. 
"""

tmp_list = [] # for saving upcoming each query
try: 

    with open (path_blast, "r") as file_blast: # read mode
    
    #---------- lil quality control
        lines = file_blast.readlines()
        content = ''.join(lines)
        if content.count(">") < 1 or content.count("Query=") < 1:
            raise ValueError("\nError: file provided must be in .blastp format\n")
    #---------- main script
    
        for line in lines:
            if line.startswith("Query="): # query 
                query = line.partition(" ")[2].partition(" ")[0].strip() # partitioning str -> get query
                
            elif line.startswith("**"): # no hits
                tmp_list.append([query, "\t\t\t"]) # still add the query, but leave it blank w/ tabs
                continue # skip to next query
                
            elif line.startswith(">"): # target
                name = line.strip(" \n>") # remove unwanted characters
                protorg = name.split("|")[2].split(" ")[0]
                protein, organism = protorg.split("_")
                
            elif line.startswith(" Score = "): # score
                score = line.partition("= ")[2].partition(" ")[0].strip() # more partitioning
                evalue = line.partition(",  ")[2].partition(" = ")[2].partition(",")[0].strip() # evalue on same line
                
            elif line.startswith(" Identities = "): # identity string
                identity = line.partition(" = ")[2].partition(" ")[2].partition(",")[0].strip(" ()%")
                tmp_list.append([query, organism, protein, evalue, identity, score]) # FINALLY, add it all in nested list

#-------------------------------------------- quality controls
    if not path_blast.endswith(".blastp"):
        raise Exception("\nError: file provided not supported. Please provide a .blastp file\n")

except ValueError as V_message:
    print(V_message)
    sys.exit()

except FileNotFoundError:
    print("\nError: file doesnt exist, make sure it's written correctly\n")
    sys.exit()

except PermissionError:
    print("\nError: file does not have adequate access rights, make sure it has the an open permission\n")
    sys.exit()

except Exception as E_message:
    print(E_message)
    sys.exit()
#%%

"""
------------------------------------------------- Output File-----------------------------------------------
Creating headers, and writing the output onto a text file.

"""
headers = ["#Query", "Organism", "Protein", "e-value", "Identity [%]", "Score"]

with open(path_output, "w") as file_output:
    file_output.write("\t".join(headers) + "\n") # headers
    for line in tmp_list:
        file_output.write("\t".join(map(str,line))) # creating a tab-sep. strs from rows of the nested list
        file_output.write("\n")
