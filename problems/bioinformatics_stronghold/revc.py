'''
ROSALIND Complementing a Strand of DNA (REVC)

Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the 
symbols of s, then taking the complement of each symbol (e.g., the reverse complement 
of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

def revc(dna_str):
    rev_complement = ''
    for i in reversed(dna_str):
        if i == "A":
            rev_complement +=  "T"
        elif i == "C":
            rev_complement += "G"
        elif i == "G":
            rev_complement += "C"
        elif i == "T":
            rev_complement += "A"
    return rev_complement

def test_revc():
    sample_in = "AAAACCCGGT"
    sample_out = "ACCGGGTTTT"
    test_out = revc(sample_in)
    print(sample_out == test_out)

if __name__ == "__main__":
    print("ROSALIND Complementing a Strand of DNA (REVC):")
    #test_revc()
    with open('../inputs/rosalind_revc.txt', 'r') as f:
        dna_str = f.readline().strip()
        print(revc(dna_str))
    