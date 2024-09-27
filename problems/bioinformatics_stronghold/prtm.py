'''
ROSALIND Calculating Protein Mass (PRTM)

Problem
In a weighted alphabet, every symbol is assigned a positive real number called a weight.
A string formed from a weighted alphabet is called a weighted string, and its weight is 
equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the
monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
'''

import sys
import os

# Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

import utils

def prtm(protein_str):
    total_weight = 0.0
    for i in protein_str:
        total_weight += utils.get_monoisotopic_mass(i)
    return total_weight

if __name__ == "__main__":
    print("ROSALIND Calculating Protein Mass (PRTM)")
    with open("../../inputs/bioinformatics_stronghold/rosalind_prtm.txt", "r") as f:
        protein_str = f.readline().strip()
        print(prtm(protein_str))
        