#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:01:52 2026
extract fasta file of each complete ??
@author: linda + claude ai
"""
import os
import glob

OUTPUT_DIR = "Results/9_busco_fastas"

SPECIES = {
    "H_tartakovskyi": {
        "full_table": "Results/8_busco/H_tartakovskyi/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/H_tartakovskyi.faa",
        "hmmer_dir":  "Results/8_busco/H_tartakovskyi/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "P_berghei": {
        "full_table": "Results/8_busco/P_berghei/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/P_berghei.faa",
        "hmmer_dir":  "Results/8_busco/P_berghei/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "P_cynomolgi": {
        "full_table": "Results/8_busco/P_cynomolgi/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/P_cynomolgi.faa",
        "hmmer_dir":  "Results/8_busco/P_cynomolgi/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "P_faciparum": {
        "full_table": "Results/8_busco/P_faciparum/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/P_faciparum.faa",
        "hmmer_dir":  "Results/8_busco/P_faciparum/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "P_knowlesi": {
        "full_table": "Results/8_busco/P_knowlesi/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/P_knowlesi.faa",
        "hmmer_dir":  "Results/8_busco/P_knowlesi/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "P_vivax": {
        "full_table": "Results/8_busco/P_vivax/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/P_vivax.faa",
        "hmmer_dir":  "Results/8_busco/P_vivax/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "P_yoelii": {
        "full_table": "Results/8_busco/P_yoelii/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/P_yoelii.faa",
        "hmmer_dir":  "Results/8_busco/P_yoelii/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    },
    "T_gondii": {
        "full_table": "Results/8_busco/T_gondii/run_apicomplexa_odb12/full_table.tsv",
        "faa":        "Results/6_nobird_annotation/T_gondii.faa",
        "hmmer_dir":  "Results/8_busco/T_gondii/run_apicomplexa_odb12/hmmer_output/initial_run_results",
    }
}



def parse_full_table(path_table):
    """
    parses: a "full_table.tsv" from BUSCO
    returns: { busco_id : seq_id } 
    only "Complete" - single-copy orthologs
    """
    dir_busco_seq = {}
    best_scores = {}
    with open(path_table) as fip:
        for line in fip:
            if not line.startswith("#"):
                id_row = line.rstrip().split("\t")
                if len(id_row)<3:
                    continue
                busco_id, status, seq_id = id_row[0], id_row[1], id_row[2]
                if status == "Complete":
                    dir_busco_seq[busco_id] = seq_id
                elif status == "Duplicated":
                    if len(id_row) > 3:
                        score = float(id_row[3]) # busco score
                    else:
                        score = 0.0
                    if len(id_row) > 4:
                        length = int(id_row[4]) # sequence length
                    else:
                        length = 0
                    if busco_id not in dir_busco_seq:
                        dir_busco_seq[busco_id] = seq_id
                        best_scores[busco_id] = (score, length)
                    else:
                        prev_score, prev_length = best_scores.get(busco_id, (0, 0))
                        if (score, length) > (prev_score, prev_length):
                            dir_busco_seq[busco_id] = seq_id
                            best_scores[busco_id] = (score, length)
                        
    return(dir_busco_seq)

def parse_faa(faa_path):
    """
    Parse a protein FASTA file.

    Returns dict: sequence_id -> sequence (string, no newlines).
    The sequence_id is everything after '>' up to the first whitespace.
    """
    dir_seq_faa = {}
    current_id = None
    with open(faa_path) as fip:
        for line in fip:
            line = line.strip()
            if line.startswith(">"):
                current_id = line[1:].split()[0]  # everything after > up to first space
                dir_seq_faa[current_id] = ""       # start empty string for this sequence
            elif current_id is not None:
                dir_seq_faa[current_id] += line    # append each sequence line
    return dir_seq_faa


def busco_id_from_hmmer_dir(hmmer_dir, busco_id):
    """
    Confirm / retrieve the full BUSCO id by looking for the .out file
    in the hmmer_output directory.  Returns the busco_id unchanged if found,
    or None if no matching file exists.

    The hmmer output files are named like: 131at5794.out
    The BUSCO id in the full_table is also 131at5794, so they match directly.
    This function is mainly a sanity-check / fallback for path discovery.
    """
    expected = os.path.join(hmmer_dir, f"{busco_id}.out")
    if os.path.isfile(expected):
        return busco_id
    # Try globbing in case the directory has subdirectories
    hits = glob.glob(os.path.join(hmmer_dir, "**", f"{busco_id}.out"), recursive=True)
    return busco_id if hits else None


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # STEP 1 - PARSE ALL FULL TABLES
    print("\nparsing full_table.tsv")
    species_buscos = {}
    for label, cfg in SPECIES.items():
        tsv = cfg["full_table"]
        if not os.path.isfile(tsv):
            raise FileNotFoundError(f"[{label}] full_table not found")
        species_buscos[label] = parse_full_table(tsv)
        n = len(species_buscos[label])
        print(f"\n {label}: {n} Complete BUSCOs")
    
    # STEP 2 - find "Complete" BUSCOs present in all sp.
    all_labels = list(SPECIES.keys())
    shared = set(species_buscos[all_labels[0]]) # give all busco ids for first species
    for label in all_labels[1:]:
        shared &= set(species_buscos[label].keys()) # save if they match
    print(f"\nBUSCOs Complete in all {len(all_labels)} species: {len(shared)}")

    if not shared:
        print("\nNo shared single-copy BUSCOs found. Check your input files.")
        return

    # STEP 3 - LOAD PROTEIN SEQUENCES
    print("\nloading protein sequences")
    species_seqs = {} 
    for label, cfg in SPECIES.items():
        faa = cfg["faa"]
        if not os.path.isfile((faa)):
            raise FileNotFoundError(f"\n[{label}], FAA file not found: {faa}")
        species_seqs[label] = parse_faa(faa)
        print(f"\n{label}: {len(species_seqs[label])} sequences loaded")
        
    # STEP 5 - WRITE A FASTA PER BUSCO
    print(f"\nWriting FASTA files to {OUTPUT_DIR}/ ..")
    written = 0
    skipped = 0
    
    for busco_id in sorted(shared):
        out_path = os.path.join(OUTPUT_DIR, f"{busco_id}.faa")
        records = []
        ok = True
        
        for label in all_labels:
            seq_id = species_buscos[label][busco_id]
            seqs = species_seqs[label]
            
            if seq_id not in seqs:
                print(f"WARNING: {label} - seq '{seq_id}' for BUSCO {busco_id} not found in FAA. Skipped.")
                ok = False
                break
            
            records.append((label, seqs[seq_id]))
            
        if not ok:
            skipped += 1
            continue
            
        with open(out_path, "w") as out:
            for label, seq in records:
                out.write(f">{label}\n")
                for i in range(0, len(seq), 60):
                    out.write(seq[i:i+60] + "\n")
        
        written += 1
            
    print(f"\n done. wrote {written} BUSCO FASTA files, skipped {skipped}.")
    print(f"\n output directory: {os.path.abspath(OUTPUT_DIR)}")
                    
                    
if __name__ == "__main__":
    main()