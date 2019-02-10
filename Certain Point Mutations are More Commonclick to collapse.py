from __future__ import division
import FastaReader as fastr

def is_purine(base):
    if base == 'A' or base == 'G':
        return True
    else:
        return False

def is_pyrimidine(base):
    if base == 'C' or base == 'T':
        return True
    else:
        return False

def ratio(s1, s2):
    transition = 0
    transversion = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if is_purine(s1[i]) and is_purine(s2[i]):
                transition += 1
            elif is_pyrimidine(s1[i]) and is_pyrimidine(s2[i]):
                transition += 1
            else:
                transversion += 1
    ratio = transition/transversion
    return ratio


seqs = fastr.read("file.txt")

s1 = seqs[0]
s2 = seqs[1]


print ratio(s1, s2)
