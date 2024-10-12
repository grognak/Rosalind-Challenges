'''
ROSALIND Completing a Tree (TREE)

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n
nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
'''

if __name__ == "__main__":
  print("ROSALIND Completing a Tree (TREE)")
  data = []                                          
  with open('../../inputs/bioinformatics_stronghold/rosalind_tree.txt', 'r') as f:
      for line in f:                                 
          split_data = [int(x) for x in line.split()]
          data.append(split_data)                    

  n = data[0][0]                                     
  edges = data[1:]                                   
  print(n - len(edges) - 1) 