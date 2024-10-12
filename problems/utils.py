def parse_fasta_file(lines):
    '''
    Parses a FASTA file and returns a list of id-sequence tuples.
    
    The FASTA id is the key in the sequence dictionary and the dna string is the value.
    The lines are assumed to be stripped of any new line characters.
    '''
    sequences = []
    temp_sequence = ""
    temp_id = ""
    for l in lines:
        if l[0] == ">":
            if temp_sequence != "":
                sequences.append((temp_id, temp_sequence))
                temp_sequence = ""
            temp_id = l[1:]
        else:
            temp_sequence += l
    sequences.append((temp_id, temp_sequence)) #last sequence in the file
    return sequences

def parse_fasta(fasta_data):
    '''
    Parses a single FASTA file and returns a tuple.
    (fasta_id, fasta_sequence)
    '''
    fasta_id = ""
    fasta_sequence = ""
    
    for line in fasta_data:
        if ">" in line:
            fasta_id = line[1:]
        else:
            fasta_sequence += line.strip()
    return fasta_id, fasta_sequence


def convert_rna_amino(codon):
    '''
    Converts the provided rna codon into an amino acid.
    '''
    rna_codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
        "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
        "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
        "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
        "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
        "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
        "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
        "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
        "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
        "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
        "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
        "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
        "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
        "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
        "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
    }
    return rna_codon[codon]

def convert_amino_rna(acid):
    RNA_codon_table = {
        'A': ('GCU', 'GCC', 'GCA', 'GCG'),
        'C': ('UGU', 'UGC'),
        'D': ('GAU', 'GAC'),
        'E': ('GAA', 'GAG'),
        'F': ('UUU', 'UUC'),
        'G': ('GGU', 'GGC', 'GGA', 'GGG'),
        'H': ('CAU', 'CAC'),
        'I': ('AUU', 'AUC', 'AUA'),
        'K': ('AAA', 'AAG'),
        'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
        'M': ('AUG',),
        'N': ('AAU', 'AAC'),
        'P': ('CCU', 'CCC', 'CCA', 'CCG'),
        'Q': ('CAA', 'CAG'),
        'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
        'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
        'T': ('ACU', 'ACC', 'ACA', 'ACG'),
        'V': ('GUU', 'GUC', 'GUA', 'GUG'),
        'W': ('UGG',),
        'Y': ('UAU', 'UAC'),
        'STOP': ('UAA', 'UAG', 'UGA'),
    }
    return RNA_codon_table[acid]

def get_monoisotopic_mass(amino_acid):
    monoisotopic_mass = {
        "A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259, 
        "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406, 
        "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293, 
        "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203, 
        "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333,
    }
    return monoisotopic_mass[amino_acid]

def reverse_complement(dna_str):
    return dna_str.translate(str.maketrans('ACGT', 'TGCA'))[::-1]