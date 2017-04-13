def read(path):
    f = open(path, "r")
    lines = f.readlines()

    seqs = []
    data = str()
    for line in lines:
        if line.startswith(">"):
            if len(data) > 0:
                seqs.append(data)
            data = str()
        else:
            data += line.rstrip()
    seqs.append(data)
    return seqs
