'''
ROSALIND Locating Restriction Sites

Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For 
instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length 
between 4 and 12. You may return these pairs in any order.
'''

fasta_formatted_string = '>Rosalind_5704CGCGGTTCAGACCACTGCGATACGTGGGACGAATCCCGGACGGCTGTTAAATGTGGGGTGCTGACCTCATATTCGCAGATGCGTGCAAAATGGCCCTAGCGATCCGCACAGAGGCATCCCGCCAGGAATCTGATGCGGCGCGTCATTCACCCTGAGACTGCGGCCCTCTGGCGGGAAGGTTCCTTCACAGCCAATTCTTGGCGAATCACTCGCACCAACGCACTTTATTGACGCAAAAGGAACATCAATTTGCGTCCCTCCTCAGCGTATGTTTGTGGCGGCCGAGTGCCGTTCCAACTGCCGCGACCAAGAACTTACGTTTCTACTAGGCAATGTATGAACCCTTGAACCACGAATACATCCGTAATACGATCGTATCACACGGCAGCTCACAATACACCGGCCTGTATCAACGAACCAAACACGGTTGGAATTCCAAAAGAAAAAATAGATTATTATTTTTAGACGGTTCAGTAAAACGAAGAGTAGTACACGAGGCAGTCCTGCAGGAGAAGCTCTTGAAGGAGCATTAATGGGAAGAGGTGCCGCGAGATCGACTGCAAGAATTTCGCTGCCCCCGCCATATTGGTGCGCGTGAATTGAGTACTCATGGGCTTCGCACTGAGAGAGAAACTTGGTGAAAGCATTGAAGAGATTAATCGTTGAATTAACACCTAGGAGATCTTCCAGAGTGTCGTGAACACGCGCATGTGTTCCGGTCGACAAATTCCTGGAGCTGGACGTCGTGGACCCCGCAGTCATTCGATTTCGGTGGAGACACGCCTGAAGCGCGGCCTCGTTTATCCGTTAGAACTAAGCCCTGCTGCACTACTTTACCCAGTGTTTTGCACTATTGCTCTTTTATA'

dna_id = fasta_formatted_string[0 : 14]
dna_seq = fasta_formatted_string[14 :]

#Function below is inspired from the REVC-Complementing-a-Strand-of-DNA.py file
def is_reverse_palindrome(sequence):

    #Take the reverse
    reversed_string = sequence[::-1]

    #Create a dictionary
    complement_dict = {'A':'T','T':'A','G':'C','C':'G'}

    #Take the compelement of the reverse
    complement_reversed_string = ""
    for base in reversed_string:
        complement_reversed_string += complement_dict[base]
    if complement_reversed_string == sequence:
        return True
    return False

length_of_dna = len(dna_seq)

#We will divide the string into 4-base, 5-base ...., 12-base length respectively with the loop below
for i in range(4, 13):
    #We will get every consecutive i-base length part
    #That is, if our string is AGAT and if we want all consecutive 2-base length parts
    #We will have AG,GA,AT
    #Loop below does exactly the same
    for j in range(length_of_dna - i + 1):

        part = dna_seq[j : j + i]
        if is_reverse_palindrome(part):
            #Position is incremented by one since question assumes first index is 1 not 0
            print(j + 1, i)