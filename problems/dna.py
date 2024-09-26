'''
ROSALIND Counting DNA Nucleotides (DNA)

Problem
A string is simply an ordered collection of symbols selected from some alphabet and 
formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G',
and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that
the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

def count_nucleotides(dna_str):
  return dna_str.count("A"), dna_str.count("C"), dna_str.count("G"), dna_str.count("T")

if __name__ == "__main__":
  test_str = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
  with open("../inputs/rosalind_dna.txt", "r") as f:
    dna_str = f.readline().strip()
    #print("ROSALIND Counting DNA Nucleotides (DNA): <Test>", count_nucleotides(test_str))
    print("ROSALING Counting DNA Nucleotides (DNA): ", count_nucleotides(dna_str))