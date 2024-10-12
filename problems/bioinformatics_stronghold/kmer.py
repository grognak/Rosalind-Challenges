'''
ROSALIND k-Mer Composition (KMER)

Problem
For a fixed positive integer k, order all possible k-mers taken from an underlying
alphabet lexicographically.

Then the k-mer composition of a string s can be represented by an array A for which 
A[m] denotes the number of times that the mth k-mer (with respect to the lexicographic
order) appears in s.

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
'''
import itertools
import re

def parse_fasta(fasta_data):
  '''
  Parses a single FASTA file and returns a tuple.
  (fasta_id, fasta_sequence)
  '''
  fasta_id = ""
  fasta_sequence = ""

  for line in fasta_data:
      if ">" in line:
          fasta_id = line[1:]
      else:
          fasta_sequence += line.strip()
  return fasta_id, fasta_sequence

if __name__ == "__main__":
  print("ROSALIND k-Mer Composition (KMER)")
  nt = 'ACGT'        #Use this order of nt to get correct order later without sorting
  permutations = itertools.product(nt, repeat=4)

  kmers = []
  for i, j in enumerate(list(permutations)):
      kmer = ''
      for item in j:
          kmer += str(item)
      kmers.append(kmer)
  
  with open("../../inputs/bioinformatics_stronghold/rosalind_kmer.txt", "r") as f:
    lines = [line.rstrip() for line in f]
    fasta = parse_fasta(lines)
    A = []
    for k in kmers:
        occurence = 0
        pattern = re.compile(r'(?=(' + k + '))')
        for l in re.findall(pattern, str(fasta[1])):
            occurence += 1
        A.append(occurence)
    print(*A, sep=' ')