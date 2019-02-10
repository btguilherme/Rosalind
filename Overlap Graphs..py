def open_fasta(path):
    f = open(path, "r")
    lines = f.readlines()
    heads = []
    seqs = []
    data = str()

    for line in lines:
        if line.startswith(">"):
        	#removes '>' with [1:len(line)] and '\n' with rstrip()
            heads.append(line[1:len(line)].rstrip())
            if len(data) > 0:
                seqs.append(data)
            data = str()
        else:
            data += line.rstrip()
    seqs.append(data)

    return heads, seqs

k = 3

heads, seqs = open_fasta("file.txt")

for s in range(len(seqs)):
	suffix = seqs[s][-k:]
	for t in range(len(seqs)):
		if not s == t:
			prefix = seqs[t][0:k]
			if suffix == prefix:
				print(heads[s], heads[t])

