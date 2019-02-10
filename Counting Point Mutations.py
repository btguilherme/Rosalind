s = "ATCTAATATTAACTACGTCCGCATGGCTCACAACAAGATTCTACGAACTGCGGACGTCCTATGCACCACGCTTTGATGCGGACAGAGGTCATAAGTCCAGTTCCAAATTCGGCATTATACCCGGGCAAGGTGTACCTAGCCTCTTGGTGCATCGCAGAAAGTGCCTCATCGATGGCGGTATTCTACAGATGCAGGCTCGAGGCCCCTCGTAGGACAGCATGGCTTGTCTTAGTGCGACTCATCTGCTTGGGACGGATTAGTTTAGGTGGAGAGATGAGCATTCGACAATTTTACGGCCAAAATCAAAGTGAAGGTGCTCTTCTTAACTTTAACACCGAATTCATTGGCCCTTGGTTGCGATACCGTGGACCCATCAGGTCGTCCTTGAATGAAATCAACGCCCAGTTTTCGTGCAAACCCAATTCAGCTGAGGTCCTACCTAAAATCCAGTGTCGGAAATGGAACAGTCGTTTCAATCAATCCGAGACACGCTGGAGCGCCTTCTGTTAGCCCAGCACCGAATCGTCTGGTATGGCTTAATTCGATGAGTAGTTTTAACACGAGTCACTGAACTACCCAAAATATCTTCACCAGGTCGGATCTCCGGGCAATAAGAGAGGTGCCTAAGGTAACCACCTGTTGCGCCAAAGTCTTCGTCAACAATACTTGGGCAGTAAGCACCAGAGTGTCGGCTCTCAGGTAGCCGGGCAATGAGGGCAAATTAGGGTCAGCATCCGATAAGAACGACGTACTGGCAGGGAGCCGCGTATAAGGTCGCGGATGTCTCGGGTACTGAAATTTACTGTGAGGTTCATCAGTGAGGGTATCTCCAACAATTTGACATCCCATCACAGCACCAGATGTCCCTGGGTTCCTCCAGTTAAGTTATTCAAATTTCACGATCCCAG"
t = "ACCCCATGTTATCTAAGGAGCCTATTCGCCCAACATGGGTGGTCGAACGAAACAAATACAGTTGCCCTCGGGCTCATTAGTAGAAATTTCCGACGATAAATTCCAACTCCAGTGTTTTTCCTGAGGAATCTAGATCAAGCATCTCTGAGCAAAGCTTAACATACAATACCGTTCAGTTGCCTTTAGAGAGGGAGACTCGAGCTCGCGCCTAGCCGATACAACCTGTTCTAAATGAGTGTCATCTGCTCAGGAGGCGTTTGTACGGGTCACGTGGTGTGGCTACGCCGGGTGCGCGTCCATACCCAATTTGCTGGAGACGTGCTTCAAAGCGAACGCGGAGTCACGTCCTTTCGTGTGCGGGACGTTGGTCCGAGTGTGGTGTGCCGCAATCAGGGCCCTGCCGAGAGTGTGGGCAAACCGAGATTACATTAGGTATTACGATGAATGCAATGTTCGAAAGGGTAAAGTCGACTCGGTCACTTCGCAATTCGTTTTGTGGCAGTCTATCGGACCTGCACTCCGTACTCTTCATGAGGTGAAAGCGATGATTAATCTTAGGTGCCTTAAGAGAGCTGACCAAAATCTCTTCGGCTCCTGCCAAAGTCTCTGTTGTAGAGCGGGCGTCTCCTTGACCAGCGGTGACTCCAAGCCGGTCAACAACAATACTTGGTCACTTCGCGGCCGCTGGGTGTGCCTAAAGCATCCGGCCTTAGAGTGAACCTTACGGTTCGTATTGTACAAAATAATCGGCCCGGATGGGAACAGCCGCTACAATGCCGGATTACCCAACGATGAGAAATACCCTGGGGTAGCATAAGTGATCTGTGCCACGGCGGTTACACATACGATAAGATAGTCACTTTGCGGGCAGTTCCCACCTGCGCAGGATTCAAAATCGACGTTTCACA"

if len(s) == len(t):
    dist = 0
    for i in range(0,len(s)):
        if s[i] != t[i]:
            dist += 1
print dist
