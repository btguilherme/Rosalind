from __future__ import print_function
import FastaReader as fread

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

def func(cont, dna, reverse_compl, i):
    if i < len(dna):
        if dna[i] == reverse_compl[i]:
            i += 1
            cont += func(cont, dna, reverse_compl, i)
            cont += 1
            return cont
        else:
            return 0
    else:
        return cont


dna = fread.read("/home/guilherme/rosalind_revp.txt")[0]
reverse = dna[::-1]
reverse_compl = complement(reverse)

print(dna)

passo = 1
i = 0
while(i < len(dna)):
    length = func(0, dna, reverse_compl, i)
    if length > 0:
        i += length
    else:
        i += 1

    if length >= 4 and length < 12:
        print (i-length+1, end=' ')
        print(length)




#for i in range(0, len(dna)):
#    cont = func(0, dna, reverse_compl, i)
#    i += cont
#    print (cont)
