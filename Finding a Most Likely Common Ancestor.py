import FastaReader as fr

seqs = fr.read('file.txt')

profile = [0] * 4
for i in range(len(profile)):
    profile[i] = [0] * len(seqs[0])

for seq in seqs:
    for i in range(len(seq)):
        if seq[i] == 'A':
            profile[0][i] += 1
        elif seq[i] == 'C':
            profile[1][i] += 1
        elif seq[i] == 'G':
            profile[2][i] += 1
        else:
            profile[3][i] += 1

alphabet = ['A', 'C', 'G', 'T']
consensus = [''] * len(profile[0])
count_consensus = [0] * len(profile[0])

for i in range(len(profile)):
    for j in range(len(profile[i])):
        if profile[i][j] > count_consensus[j]:
            count_consensus[j] = profile[i][j]
            consensus[j] = alphabet[i]

print(''.join(consensus))

for i in range(len(profile)):
    print(alphabet[i], end=': ')
    for j in range(len(profile[i])):
        print(profile[i][j], end=' ')
    print()
