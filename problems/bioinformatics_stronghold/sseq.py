'''
ROSALIND Finding a Spiced Motif (SSEQ)

Given: Two DNA strings s  and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence
of s. If multiple solutions exist, you may return any one.
'''

def parse_fasta_file(lines):
  '''
  Parses a FASTA file and returns a dictionary of sequences.

  The FASTA id is the key in the sequence dictionary and the dna string is the value.
  The lines are assumed to be stripped of any new line characters.
  '''
  sequences = []
  temp_sequence = ""
  temp_id = ""
  for l in lines:
      if l[0] == ">":
          if temp_sequence != "":
              sequences.append((temp_id, temp_sequence))
              temp_sequence = ""
          temp_id = l[1:]
      else:
          temp_sequence += l
  sequences.append((temp_id, temp_sequence)) #last sequence in the file
  return sequences

def sseq(s, t):
    pos = 0                                    
    positions = []                             
    for i in range(len(t)):                    
        for j in range(pos, len(s)):           
            pos += 1                           
            if len(positions) < len(t):        
                if t[i] == s[j]:               
                    positions.append(pos)      
                    break                      
    print(*positions, sep=' ')     

if __name__ == "__main__":
  print("ROSALIND Finding a Spiced Motif (SSEQ)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_sseq.txt", "r") as f:
    lines = [line.rstrip() for line in f]
    fasta_data = parse_fasta_file(lines)
    full_str = fasta_data[0][1]
    sub_str = fasta_data[1][1]
    print(full_str)
    print(sub_str)
      
    res = sseq(full_str, sub_str)