'''
ROSALIND Introduction to Random Strings (PROB)

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 
numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common 
logarithm of the probability that a random string constructed with the GC-content found
in A[k] will match s exactly.

Sample Dataset
ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783

Sample Output
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
'''
import math

def prob(dna_str, number_str):
  results = []
  for i in number_str:
    prob = 0
    chances = {
        'A' : (1-i)/2,
        'C' : i/2,
        'G' : i/2,
        'T' : (1-i)/2
    }
    for c in dna_str:
      prob = prob + math.log10(chances[c])
    results.append(prob)
  return results

if __name__ == "__main__":
  print("ROSALIND Introduction to Random Strings (PROB)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_prob.txt", "r") as f:
    dna_str = f.readline().strip()
    number_str = f.readline().strip()
    gcc = [float(i) for i in number_str.split()]
    result = []
    result = prob(dna_str, gcc)
    print(result)