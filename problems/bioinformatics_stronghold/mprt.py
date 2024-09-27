'''
ROSALIND Finding a Protein Motif (MPRT)

Problem
To allow for the presence of its varying forms, a protein motif is represented by a 
shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X."
For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access 
ID "uniprot_id" in the UniProt database, by inserting the ID number into
    http://www.uniprot.org/uniprot/uniprot_id

Alternatively, you can obtain a protein sequence in FASTA format by following
    http://www.uniprot.org/uniprot/uniprot_id.fasta

For example, the data for protein B5ZC00 can be found at 
    http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID
followed by a list of locations in the protein string where the motif can be found.
'''
from urllib.request import urlopen
from urllib.error import HTTPError

import re

def parse_fasta(id, fasta_data):
    fasta_id = ""
    fasta_sequence = ""
    
    for line in fasta_data:
        if ">" in line:
            fasta_id = id
        else:
            fasta_sequence += line.strip()
    return fasta_id, fasta_sequence

def mprt(fasta):
    locations = []
    n_glycoslylation = re.compile(r'(?=(N[^P][ST][^P]))')
    result = re.finditer(n_glycoslylation, fasta[1])
    for i in result:
        locations.append(i.span()[0]+1)
    return locations

if __name__ == "__main__":
    print("ROSALIND Finding a Protein Motif (MPRT)")
    output = ""
    with open("../../inputs/bioinformatics_stronghold/rosalind_mprt.txt", "r") as f:
        accessIds = [line.rstrip() for line in f]
        for i in accessIds:
            try:
                url = "http://www.uniprot.org/uniprot/" + i.split("_")[0] + ".fasta"
                fasta_data = []
                for line in urlopen(url):
                    fasta_data.append(line.decode('utf-8').strip())
                fasta = parse_fasta(i, fasta_data)
                locations = mprt(fasta)
                if locations:
                    output += i + "\n" + " ".join(str(x) for x in locations) + "\n"    
            except HTTPError as e:
                if e.code == 404:
                    print("Page Not Found: ", i)
                elif e.code == 400:
                    print("Bad Request: ", i)
                else:
                    raise
    print(output)
    #Get the protein sequence in FASTA format
    #Get a regex formula for N-glycostation motif
    #Search each protein sequence for the motif
    #Record each location