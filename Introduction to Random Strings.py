from __future__ import division
import math
import functools as func
import operator

s = 'ACGATACAA'
A = list('0.129 0.287 0.423 0.476 0.641 0.742 0.783'.split(' '))

for gc_content in A:
    probs = []
    for base in s:
        if base == 'A' or base == 'T':
            probs.append((1 - float(gc_content)) / 2)
        else:
            probs.append(float(gc_content) / 2)

    aux = probs[0]
    for i in range(1,len(probs)):
        aux *= probs[i]

    print('%.3f' % math.log10(aux), end=' ')