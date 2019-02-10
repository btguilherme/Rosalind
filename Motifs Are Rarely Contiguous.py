import FastaReader as fastr

seqs = fastr.read("file.txt")

s = seqs[0] #sequence
t = seqs[1] #pattern

locations = []
aux = 0

for i in range(0, len(t)):
    for j in range(aux, len(s)):
        if t[i] == s[j]:
            locations.append(j+1)
            aux = (j+2)
            break

for location in locations:
    print location
