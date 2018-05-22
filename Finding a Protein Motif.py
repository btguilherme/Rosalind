import urllib.request

seqs_names = open('file.txt', 'r')

for seq_name in seqs_names:

    path = 'http://www.uniprot.org/uniprot/' + seq_name.rstrip() + '.fasta'

    with urllib.request.urlopen(path) as response:
        seq = str(response.read()).split('\\n')
        seq_final = str()

        for i in range(1, (len(seq) - 1)):
            seq_final = seq_final + seq[i]

        seq_final_list = list(seq_final)

        indexes = []
        for i in range(len(seq_final_list)):
            if seq_final_list[i] == 'N':
                try:
                    if seq_final_list[i+1] != 'P':
                        if seq_final_list[i + 2] == 'S' or seq_final_list[i + 2] == 'T':
                            if seq_final_list[i + 3] != 'P':
                                indexes.append(i+1)
                except IndexError:
                    #nothing to do
                    nothing = 0

        if len(indexes) != 0:
            print(seq_name, end = '')
            for index in indexes:
                print(index, end = ' ')
            print()