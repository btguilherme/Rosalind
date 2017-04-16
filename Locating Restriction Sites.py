from __future__ import print_function
import FastaReader as fread
import re

def complement(reverse):
    reverse_compl = ''
    for base in reverse:
        if base == 'A':
            reverse_compl += 'T'
        elif base == 'T':
            reverse_compl += 'A'
        elif base == 'G':
            reverse_compl += 'C'
        else:
            reverse_compl += 'G'
    return reverse_compl


dna = fread.read("/home/guilherme/rosalind_revp.txt")[0]
#dna = "TCAATGCATGCGGGTCTATATGCAT"

for i in range(0, len(dna)):
    for j in range(4, 12 + 1):

        if i+j > len(dna):
            break

        frag_dna = dna[i:i+j]
        frag_dna_rev_compl = frag_dna[::-1]
        frag_dna_rev_compl = complement(frag_dna_rev_compl)

        if frag_dna == frag_dna_rev_compl:
            print (i+1, end=' ')
            print (j)
