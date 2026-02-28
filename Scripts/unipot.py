import requests
import time

# Read your abbreviations
with open("blastp_unique.txt") as f:
    abbrevs = [line.split()[1] for line in f if line.strip()]

birds = []

for abbrev in abbrevs:
    url = f"https://rest.uniprot.org/taxonomy/search?query=mnemonic:{abbrev}&fields=lineage,mnemonic"
    response = requests.get(url)
    data = response.json()
    
    if data.get("results"):
        lineage = str(data["results"][0])
        if "Aves" in lineage: # change for lineage
            birds.append(abbrev)
            print(f"{abbrev} is a bird!")
    
    time.sleep(0.2)  # be nice to the API

print("\nAll birds found:", birds)