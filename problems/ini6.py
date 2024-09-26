'''
ROSALIND Dictionaries (INI6)

Problem
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by 
spaces. Words are case-sensitive, and the lines in the output can be in any order.
'''

def get_word_count(s):
  word_count = {}
  for w in s.split(" "):
      if w not in word_count:
          word_count[w] = 0
      word_count[w] += 1
  return word_count

if __name__ == "__main__":
  with open("../inputs/rosalind_ini6.txt", "r") as f:
      s = f.readline().strip()
  word_count = get_word_count(s)
  for k,v in word_count.items():
      print(k, v)