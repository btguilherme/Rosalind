s="CGGGACATTGGGGGTTGGCTATGGCGCCAGCGCCGAAAGCGCATCCGGCACCTACGGAAGATATGAGTCCACCAGTTGTTATGCAGTGACATGCCACGCACAGTGAACCCAAGAGTCTTACTGTGTTCATTGAATACGCTCCAACCCTACACGCGTATTAGGGTTAAATTCACTAGCACATGTCGTTGTTCACACTTGCCCAAAGCAACATCATGCTATGACGACCATCACCACTGCGCTTGATATGGCTGGCGGCTGTTCACTAGCTAACATTCTCGTGTATCTATAGATAGGCTCACCGAGCAGTAGCAAAAACGAGGAGCCATGTACTAGCAATATATTGAGTATAGCGTACCACGACAGTGTGCTGTATGTTTAAACCTGCTAAGGAACATCAGGGTTGGTAAATATTAAGAGTTCTTGATAGATACGTATACAAGCTAATATTAGGGGAGGTATCATCCCGGAAACATTATTGCACTGGGAAACTCGCGGGGGCATGCATATTCAATTGTGGATAGCAATTTAATGTGTCTGGGGCGTCTTAACGCTGACGACATTCCTGCCGTCAGGGCAAGCCTTCTGCTCGAAGGTTGATGTCATTGCTGCAAGCCACGTAGACAGCAACCGCACTGTTCGTCCAGTCTGAGGTCTAAGAACACTCTAAAGTTTGGCTCATCTCGACTTCCAACCAAGGGGGCGTCGGCGATGTACACCAACGACTTCCGACCTGGTAGGAATCTTAGTTTTCTACTACCAAATGTCCCGCTATGAGAACAGTTCTGGCGATACTGAATATACGCGCCGATACGCCTCACTTAGTGGTGAG"
s=s.upper()
a=0
c=0
g=0
t=0
for base in s:
    if base == 'A':
        a+=1
    elif base == 'C':
        c+=1
    elif base == 'G':
        g+=1
    elif base == 'T':
        t+=1
string=""
string += `a`
string += ' '
string += `c`
string += ' '
string += `g`
string += ' '
string += `t`
print a
print c
print g
print t