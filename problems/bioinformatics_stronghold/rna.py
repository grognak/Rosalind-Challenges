'''
ROSALIND - Transcribing DNA into RNA (RNA)

Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is
formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''

def transcribe_rna(dna_str):
    return dna_str.replace("T", "U")

if __name__ == "__main__":
    sample_in = "GATGGAACTTGACTACGTAAATT"
    sample_out = "GAUGGAACUUGACUACGUAAAUU"
    #output = transcribe_rna(sample_in)
    #print("ROSALING Counting DNA Nucleotides (DNA): ", output == sample_out)
    with open("../inputs/rosalind_rna.txt", "r") as f:
        dna_str = f.readline().strip()
        rna_str = transcribe_rna(dna_str)
        print("ROSALIND Transcribe DNA into RNA: ", rna_str)