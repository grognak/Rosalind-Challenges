'''
ROSALIND Enumerating Oriented Gene Orderings (SIGN)

A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in
which each integer is then provided with either a positive or egative sign (for the sake
of simplicity, we omit the positive sign). For xample, π=(5,−3,−2,1,4) is a signed 
permutation of length 5.

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all 
such permutations (you may list the signed permutations in any order).
'''
from itertools import permutations, product

if __name__ == "__main__":
  print("ROSALIND Enumerating Oriented Gene Orderings (SIGN)")
  with open("../../inputs/bioinformatics_stronghold/rosalind_sign.txt", "r") as f:
    n = int(f.readline().strip())
    permutation = []                                                           
    nr = 0                                                                     
    for i in permutations(list(range(1, n + 1))):                    
        for j in product([-1, 1], repeat=len(list(range(1, n + 1)))):
            perm = [a * sign for a, sign in zip(i, j)]                         
            permutation.append(perm)                                           
            nr += 1                                                            

    print(nr)                                                                  

    for i in range(len(permutation)):                                          
        print(*permutation[i], sep=' ') 