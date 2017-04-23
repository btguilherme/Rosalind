import FastaReader as fastr
import Nucleotide2Protein as n2p

def remove_introns(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna

def make_nucleotides(trna):
    nucleotides = []
    for i in range(0, len(trna), 3):
        nucleotides.append(trna[i]+trna[i+1]+trna[i+2])
    return nucleotides

seqs = fastr.read('file.txt')
dna, introns = seqs[0], seqs[1:]
dna = remove_introns(dna, introns)
trna = dna.replace("T", "U")
nucleotides = make_nucleotides(trna)

protein = ""
for nucleotide in nucleotides:
    protein += n2p.pattern(nucleotide)
print protein
