'''
ROSALIND Transitions and Transversions (TRAN)

Problem
For DNA strings s1 and s2 having the same length, their transition/transversion ratio
R(s1,s2) is the ratio of the total number of transitions to the total number of 
transversions, where symbol substitutions are inferred from mismatched corresponding
symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
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

def tran(s1, s2):
  transition = 0                               
  transversion = 0                             
  AG = ['A', 'G']                              
  CT = ['C', 'T']                              
  for nt1, nt2 in zip(s1, s2):                 
      if nt1 != nt2:                           
          if nt1 in AG and nt2 in AG:          
              transition += 1                  
          elif nt1 in CT and nt2 in CT:        
              transition += 1                  
          else:                                
              transversion += 1                
  print('%0.11f' % (transition / transversion))

if __name__ == "__main__":
  print("ROSALIND Transitions and Transversions (TRAN)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_tran.txt", "r") as f:
    lines = [line.rstrip() for line in f]
    fasta_data = parse_fasta_file(lines)
    s1 = fasta_data[0][1]
    s2 = fasta_data[1][1]
    tran(s1, s2)
    