#!/usr/bin/env python

## Interactive program that reverse complements a string of nucleotides

def complement(seq):
    result = ""
    for base in seq:
        if base == "A":
            result += "T"
        elif base == "C":
            result += "G"
        elif base == "G":
            result += "C"
        elif base == "T":
            result += "A"
    return result

def reverse_complement(seq):
    reversed_seq = seq[::-1]
    return complement(reversed_seq)

original_sequence = raw_input("Enter the sequence to be reverse complemented: ")
new_sequence = reverse_complement(original_sequence)
print(new_sequence)
