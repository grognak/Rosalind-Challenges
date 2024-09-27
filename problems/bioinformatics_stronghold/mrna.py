'''
ROSALIND Inferring mRNA from Protein (MRNA)

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been 
translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein 
translation.)
'''
import sys
import os

# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

import utils

def mrna(protein_str):
    translations = 1
    for i in protein_str:
        translations *= len(utils.convert_amino_rna(i))
    translations *= len(utils.convert_amino_rna('STOP')) #Don't forget STOP
    return translations % 1000000

if __name__ == "__main__":
    print("ROSALIND Inferring mRNA from Protein (MRNA)")
    with open("../../inputs/bioinformatics_stronghold/rosalind_mrna.txt", "r") as f:
        protein_str = f.readline().strip()
        print(mrna(protein_str))