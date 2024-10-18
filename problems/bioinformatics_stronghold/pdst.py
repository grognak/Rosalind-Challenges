'''
ROSALIND Creating a Distance Matrix - PDST

Problem
For two strings s1 and s2 of equal length, the p-distance between them, denoted 
dp(s1,s2), is the proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by 
genetic strings), we may encode the distances between pairs of taxa via a distance matrix
D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). 
Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always,
note that your answer is allowed an absolute error of 0.001.
'''
from Bio import SeqIO

def pdst(s1, s2):
    n = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            n += 1
    return '%.5f'% (float(n)/len(s1))

if __name__ == "__main__":
    seq_name, seq_string = [], []
    print("ROSALIND Creating a Distance Matrix - PDST")
    with open("../../inputs/bioinformatics_stronghold/rosalind_pdst.txt", "r") as f:
        for seq_record in SeqIO.parse(f, "fasta"):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    for i in range(len(seq_name)):
        for j in range(len(seq_name)):
            print(pdst(seq_string[i], seq_string[j]), end=" ")
        print('')