amino_acid = {"I":3, "L":6, "V":4, "F":2, "M":1, "C":2, "A":4, "G":4,
	"P":4, "T":4, "S":6, "Y":2,	"W":1, "Q":2, "N":2, "H":2, "E":2,
	"D":2, "K":2, "R":6}

f = open("file.txt", "r")
lines = f.readlines()
a = 3 # stop condon has 3 different possibles
n = 1000000
for line in lines:
	for char in line.rstrip():
		a *= amino_acid.get(char)

print(a%n)