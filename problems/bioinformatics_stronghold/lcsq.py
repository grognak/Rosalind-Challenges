recs = rosalind_utils.read_fasta("rosalind_lcsq.txt")
seqa, seqb = recs[0][1], recs[1][1]
# return the set of all longest common subsesquences
C = rosalind_utils.lcsq(seqa, seqb)
print rosalind_utils.lcsq_len(C)
print rosalind_utils.lcsq_backtrack(C, seqa, seqb, len(seqa), len(seqb))