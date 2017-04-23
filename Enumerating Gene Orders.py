from __future__ import print_function
import itertools

def fat(n):
   if n <= 1:
      return 1
   else:
      return n * fat(n - 1)

value = 5
values = ''

for i in range(1, value+1):
    values += str(i)

perms = list(itertools.permutations(values, value))

print (fat(value))
for i in range(0, fat(value)):
    for j in range(0, value):
        print (perms[i][j], end=' ')
    print ("")
