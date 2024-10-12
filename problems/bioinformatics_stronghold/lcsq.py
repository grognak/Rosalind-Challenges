'''
ROSALIND Finding a Shared Spliced Motif (LCSQ)

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you 
may return any one.)
'''

from problems.utils import parse_fasta_file

def lcsq(x, y, m, n):
  if m == 0 or n == 0:
     return 0
  elif x[m-1] == y[n-1]:
     return 1 + lcsq(x, y, m-1, n-1)
  else:
     return max(lcsq(x, y, m, n-1), lcsq(x, y, m-1, n))
  

if __name__ == "__main__":
  print("ROSALIND Finding a Shared Spliced Motif (LCSQ)")
  with open("./inputs/bioinformatics_stronghold/rosalind_lcsq.txt", "r") as f:
    lines = [line.rstrip() for line in f]
    dna_strs = parse_fasta_file(lines)
    print(lcsq(dna_strs[0][1], dna_strs[1][1], len(dna_strs[0][1]), len(dna_strs[1][1])))