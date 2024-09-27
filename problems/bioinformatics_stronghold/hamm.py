'''
ROSALIND Counting Point Mutations (HAMM)

Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted
dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''

def hamm(s, t):
    hamm_dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamm_dist += 1
    return hamm_dist


if __name__ == "__main__":
    print("ROSALIND Counting Point Mutations (HAMM)")
    with open("../inputs/rosalind_hamm.txt", "r") as f:
        lines = [line.rstrip() for line in f]
        print(hamm(lines[0], lines[1]))