import FastaReader as fastr

def make_motifs(dna_string):
    motifs = []
    for i in range(0, len(dna_string)+1):
        for j in range(i+1, len(dna_string)+1):
            motifs.append(dna_string[i:j])
    return motifs

seqs = fastr.read("file.txt")
motifs = make_motifs(seqs[0])
saved_motif = ""
cont = 0

for motif in motifs:
    for i in range(1, len(seqs)):
        if seqs[i].find(motif) != -1:
            cont += 1
    if cont == len(seqs)-1 and len(saved_motif) < len(motif):
        saved_motif = motif
    cont = 0

print saved_motif
