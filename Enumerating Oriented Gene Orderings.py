# apaguei a versão que desenvolvi, então peguei essa no site... =(

import itertools as it

n = 6

ints = [p for p in it.permutations(range(1, n+1))]
dirs = [c for c in it.product([1,-1], repeat = n)]

print(len(ints)*len(dirs))

for i in ints:
    for d in dirs:
       print(' '.join([str(a*b) for a, b in zip(i, d)]))