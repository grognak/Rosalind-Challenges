'''
ROSALIND Translating RNA into Protein (PROT)

Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the 
English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are 
constructed from these 20 symbols. Henceforth, the term genetic string will incorporate
protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into
the amino acid alphabet.

Given: An RNA string s  corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''

from utils import convert_rna_amino

def prot(rna_str):
    prot_str = ""
    for i in range(0, len(rna_str)-1, 3):
        prot = convert_rna_amino(rna_str[i:i+3])
        if prot == "STOP":
            return prot_str
        prot_str += prot
    return prot_str

if __name__ == "__main__":
    print("ROSALIND Translating RNA into Protein (PROT)")
    sample_data = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    sample_out = "MAMAPRTEINSTRING"
    #print (prot(sample_data))
    with open("../inputs/rosalind_prot.txt", "r") as f:
        print(prot(f.readline().strip()))