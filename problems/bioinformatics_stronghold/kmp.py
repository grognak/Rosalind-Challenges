'''
ROSALIND Speeding up Motif Finding (KMP)

A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring
s[k:n].

The failure array of s is an array P of length n for which P[k] is the length of the
longest substring s[j:k] that is equal to some prefix s[1:k−j+1], where j cannot equal 1
(otherwise, P[k] would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
'''

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

def kmp(dna_str):
  n = len(dna_str)
  arr = [0] * n
  for i in range(1, n):
      j = arr[i - 1]
      while j > 0 and dna_str[i] != dna_str[j]:
          j = arr[j - 1]
      if dna_str[i] == dna_str[j]:
          j += 1
      arr[i] = j
  return arr

if __name__ == "__main__":
  print("ROSALIND Speeding up Motif Finding (KMP)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_kmp.txt", "r") as f:
    input = [line.rstrip() for line in f]
    pair = parse_fasta(input)
    print(" ".join(map(str, kmp(pair[1]))))