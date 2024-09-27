'''
ROSALIND Consensus and Profile (CONS)

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA
format.

Return: A consensus string and profile matrix for the collection. (If several possible
consensus strings exist, then you may return any one of them.)
'''

from utils import parse_fasta

def cons(fasta):
    sequence_length = len(list(fasta.values())[0])
    profile_matrix = {
        "A": [0] * sequence_length,
        "C": [0] * sequence_length,
        "G": [0] * sequence_length,
        "T": [0] * sequence_length    
    }
    
    for dna_str in fasta:
        for i in range(0, sequence_length):
            if fasta[dna_str][i] == "A":
                profile_matrix["A"][i] += 1
            elif fasta[dna_str][i] == "C":
                profile_matrix["C"][i] += 1
            elif fasta[dna_str][i] == "G":
                profile_matrix["G"][i] += 1
            elif fasta[dna_str][i] == "T":
                profile_matrix["T"][i] += 1
    
    consensus = []
    for j in range(sequence_length):
        max_count = -1
        max_nucleotide = ''
        for nucleotide in "ACGT":
            if profile_matrix[nucleotide][j] > max_count:
                max_count = profile_matrix[nucleotide][j]
                max_nucleotide = nucleotide
        consensus.append(max_nucleotide)
    return ''.join(consensus), profile_matrix
        

if __name__ == "__main__":
    print("ROSALIND Consensus and Profile (CONS)")
    with open("../inputs/rosalind_cons.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        fasta = parse_fasta(lines)
        consensus, profile_matrix = cons(fasta)
        print(consensus)
        print("A:", ' '.join(map(str, profile_matrix['A'])))
        print("C:", ' '.join(map(str, profile_matrix['C'])))
        print("G:", ' '.join(map(str, profile_matrix['G'])))
        print("T:", ' '.join(map(str, profile_matrix['T'])))