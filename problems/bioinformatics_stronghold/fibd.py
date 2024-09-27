'''
ROSALIND Mortal Fibonacci Rabbits

Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, 
which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits
reaches maturity in one month and produces a single pair of offspring (one male, one 
female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming
solution in the case that all rabbits die out after a fixed number of months.

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if 
all rabbits live for m months.
'''

def fibd(n, m):
    ages = [1] + [0]*(m-1)
    for i in range(n-1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

if __name__ == "__main__":
    print("ROSALIND Mortal Fibonacci Rabbits")
    with open("../../inputs/bioinformatics_stronghold/rosalind_fibd.txt", "r") as f:
        n, m = f.readline().strip().split(" ")
        print(fibd(int(n), int(m)))