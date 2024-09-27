'''
Problem
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset: 100 200
Sample Output: 7500
'''

def sum_odds(start, end):
  a = 0
  for i in range(start, end+1):
    if i % 2 != 0:
      a = a + i
  return a

if __name__ == "__main__":
  with open("../inputs/rosalind_ini4.txt", "r") as f:
    start, end = map(int, f.readline().strip().split())
    #print("ROSALIND Conditions and Loops (INI4): <Test> ", sum_odds(100, 200))
    print("ROSALIND Conditions and Loops (INI4): ", sum_odds(start, end))