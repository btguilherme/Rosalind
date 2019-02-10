from __future__ import division
import FastaReader as fastr

seqs = fastr.read("file.txt")

gc_content = 0
head = ""

for i in range(0,len(seqs)):
    no_g = seqs[i].replace("G",'')
    no_gc = no_g.replace("C",'')

    pct = (100 * (len(seqs[i]) - len(no_gc)))/len(seqs[i])

    if pct > gc_content:
        gc_content = pct
        head = fastr.heads[i]

print head
print gc_content
