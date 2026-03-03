# made by AI !
# script that finds out if e.g. the organism from swissformat: Q42290|MPPB_ARATH, belong to a certain phylum

import requests
import time

# Read your abbreviations
with open("output/new_blastp_table.txt") as f:
    abbrevs = list(set(line.split()[1] for line in f if line.strip() and not line.startswith("#") and len(line.split()) > 1))

birds = []

for abbrev in abbrevs:
    url = f"https://rest.uniprot.org/taxonomy/search?query=mnemonic:{abbrev}&fields=lineage,mnemonic"
    response = requests.get(url)
    data = response.json() # this converts to python dictionary
    
    if data.get("results"):
        lineage = str(data["results"][0])
        if "Aves" in lineage: # change for lineage (Aves for birds right now)
            birds.append(abbrev)
            print(f"{abbrev} is a bird!")
    
    time.sleep(0.2)  # be nice to the API

print("\nAll birds found:", birds)