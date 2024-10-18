'''
ROSALIND Ordering Strings of Varying Length Lexicographically (LEXV)

Problem
Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring 
t′=t[1:m]. We have two cases:
    If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
    Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′ (e.g.,
    APPLET<LexARTS because APPL<LexARTS).
Given: A permutation of at most 12 symbols defining an ordered alphabet A and a 
positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. 
(Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on 
the order in which the symbols are given.)
'''

def alpha_combs(alphabet, n, acc='', res=[]):
    if n > 0:
        for c in alphabet:
            res.append(acc + c)
            alpha_combs(alphabet, n - 1, acc + c, res)
    return res


def result(s, size):
    bits = s.split()
    return alpha_combs(bits, size)

if __name__ == "__main__":
    dataset = []
    size = 0
    print("ROSALIND Ordering Strings of Varying Length Lexicographically (LEXV)")
    with open('../../inputs/bioinformatics_stronghold/rosalind_lexv.txt', 'r') as f:
        dataset = f.readline().strip()
        size = int(f.readline().strip())
    with open("../../inputs/bioinformatics_stronghold/rosalind_lexv_out.txt", "w") as f:
        f.write("\n".join(result(dataset, size)))
        f.close()