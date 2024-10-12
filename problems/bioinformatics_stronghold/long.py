'''
ROSALIND Genome Assembly as Shortest Superstring (LONG)

Problem
For a collection of strings, a larger string containing every one of the smaller strings
as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of 
reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in
FASTA format (which represent reads deriving from the same strand of a single linear
chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way
to reconstruct the entire chromosome from these reads by gluing together pairs of reads
that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a
reconstructed chromosome).
'''

'''
1  Read file and create tuples of FASTA ID and FASTA String
2  Let FASTA String[] be given set of strings.
3  Create an auxiliary array of strings, temp[].  Copy contents
   of FASTA String[] to temp[]
4  While temp[] contains more than one strings
     a) Find the most overlapping string pair in temp[]. Let this
        pair be 'a' and 'b'. 
     b) Replace 'a' and 'b' with the string obtained after combining
        them.
5  The only string left in temp[] is the result, return it.
'''
import sys

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
  

def minimum(a, b):
  return a if a < b else b


def findOverlappingPair(str1, str2):
  # Max will store maximum 
  # overlap i.e maximum
  # length of the matching 
  # prefix and suffix
  max_len = -sys.maxsize
  len1 = len(str1)
  len2 = len(str2)
  str_ = ""

  # Check suffix of str1 matches
  # with prefix of str2
  for i in range(1, minimum(len1, len2)+1):
      # Compare last i characters 
      # in str1 with first i
      # characters in str2
      if str1[len1-i:] == str2[:i]:
          if max_len < i:
              # Update max and str_
              max_len = i
              str_ = str1 + str2[i:]

  # Check prefix of str1 matches 
  # with suffix of str2
  for i in range(1, minimum(len1, len2)+1):
      # compare first i characters 
      # in str1 with last i
      # characters in str2
      if str1[:i] == str2[len2-i:]:
          if max_len < i:
              # Update max and str_
              max_len = i
              str_ = str2 + str1[i:]

  return max_len, str_


def long(fasta_data):
  arr = []
  for i in fasta_data:
    arr.append(i[1])
  n = len(arr)
  # Run n-1 times to 
  # consider every pair
  while n != 1:
      # To store  maximum overlap
      max_len = -sys.maxsize   
      # To store array index of strings
      l, r = 0, 0    
      # Involved in maximum overlap
      res_str = ""    

      # Maximum overlap
      for i in range(n):
          for j in range(i+1, n):
              str_ = ""
              # res will store maximum 
              # length of the matching
              # prefix and suffix str is 
              # passed by reference and
              # will store the resultant 
              # string after maximum
              # overlap of arr[i] and arr[j], 
              # if any.
              res, str_ = findOverlappingPair(arr[i], arr[j])

              # check for maximum overlap
              if max_len < res:
                  max_len = res
                  res_str = str_
                  l, r = i, j

      # Ignore last element in next cycle
      n -= 1   

      # If no overlap, append arr[n-1] to arr[0]
      if max_len == -sys.maxsize:
          arr[0] += arr[n]
      else:
          # Copy resultant string to index l
          arr[l] = res_str
          # Copy string at last index to index r
          arr[r] = arr[n]

  return arr[0]
    
  

if __name__ == "__main__":
  print("ROSALIND Genome Assembly as Shortest Superstring (LONG)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_long.txt",
            "r") as f:
    lines = [line.rstrip() for line in f]
    fasta_data = parse_fasta_file(lines)
    print(long(fasta_data))