n = 29
k = 5

kids = 0
rep = 0

for month in range(1, n+1):
    if month == 1:
        kids = 1
    else:
        aux = 0
        if kids != 0:
            rep += kids
            aux = kids
            kids = 0
        if rep - aux != 0:
            kids += (rep - aux) * k

print(kids+rep)
