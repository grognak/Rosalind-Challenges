'''
ROSALIND Longest Increasing Subsequence (LGIS)

Problem
A subsequence of a permutation is a collection of elements of the permutation in the
order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing 
if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 
9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 
4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing 
subsequence of π.
'''

data = open('../../inputs/bioinformatics_stronghold/rosalind_lgis.txt', 
            'r').read().splitlines()

maxnum = int(data[0])
perm   = [int(x) for x in data[1].split()]

def lgis(maxnum, perm):
  levels = []
  graph  = {}
  for i in perm:
    if len(levels) == 0:
      levels.append([i])
      graph[i] = 0
    else:
      for lev in reversed(range(len(levels) + 1)):
        if i in graph.keys():
          break
        if lev == 0:
          levels[0].append(i)
          graph[i] = 0
          break
        lower_lev = levels[lev-1]
        lt = [x for x in lower_lev if x < i]
        if len(lt) > 0:
          if len(levels) == lev:
            levels.append([i])
          else:
            levels[lev].append(i)
            lev_gt = [x for x in levels[lev] if x > i]
            levels[lev] = list(set(levels[lev]).difference(set(lev_gt)))
          graph[i] = lt[0]

# Get now the returned answer table

  res = []
  i = levels[-1][0]
  while(i != 0):
    res.append(i)
    i = graph[i]
  res = list(reversed(res))
  return res

print(" ".join([str(x) for x in lgis(maxnum, perm)]))
print(" ".join(
  list(reversed([str(x) for x in lgis(maxnum, list(reversed(perm)))]))))