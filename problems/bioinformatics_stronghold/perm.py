'''
ROSALIND Enumerating Gene Orders (PERM)

Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example,
π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such 
permutations (in any order).
'''
import math
from itertools import permutations

if __name__ == "__main__":
    print("ROSALIND Enumerating Gene Orders (PERM)")
    n = 6
    print(math.factorial(n))
    for i in permutations(range(1, n+1)):
        print(' '.join(map(str, i)))