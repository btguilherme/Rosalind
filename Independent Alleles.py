import math

k = 6
n = 18

N = 2**k
res = 0
for i in range(n,N+1):
    res += ((math.factorial(N))/(math.factorial(i)*math.factorial(N-i))) * 0.25**i * 0.75**(N - i)
print("%.3f" % res)
