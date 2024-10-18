with open("../../inputs/bioinformatics_stronghold/rosalind_eval.txt", "r") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
    A = map(float, f.readline().strip().split(" "))

at = s.count('A') + s.count('T')
gc = s.count('G') + s.count('C')
for i in A:
    print(pow((1-i)/2, at) * pow(i/2, gc) * (n-len(s)+1), end=" ")
print()  