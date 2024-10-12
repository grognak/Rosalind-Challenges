'''
ROSALIND Perfect Matchings and RNA Secondary Structures (PMCH)

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 
U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding 
graph of s.
'''
from math import factorial

def pmch(rna_str):
  return factorial(rna_str.count('U')) * factorial(rna_str.count('G'))

if __name__ == "__main__":
  print("ROSALIND Perfect Matchings and RNA Secondary Structures (PMCH)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_pmch.txt", "r") as f:
    f.readline()
    rna_str = f.readline().strip()
    print(pmch(rna_str))