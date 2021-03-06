def pattern(codon):
    if codon == 'GCU'	or codon == 'GCC'	or codon == 'GCA'	or codon == 'GCG':
        return 'A'
    elif codon == 'UGU' or codon == 'UGC':
        return 'C'
    elif codon == 'GAU' or codon == 'GAC':
        return 'D'
    elif codon == 'GAA' or codon == 'GAG':
        return 'E'
    elif codon == 'UUU' or codon == 'UUC':
        return 'F'
    elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
        return 'G'
    elif codon == 'CAU' or codon == 'CAC':
        return 'H'
    elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
        return 'I'
    elif codon == 'AAA' or codon == 'AAG':
        return 'K'
    elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
        return 'L'
    elif codon == 'AUG':
        return 'M'
    elif codon == 'AAU' or codon == 'AAC':
        return 'N'
    elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
        return 'P'
    elif codon == 'CAA' or codon == 'CAG':
        return 'Q'
    elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
        return 'R'
    elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
        return 'S'
    elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
        return ''
    elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
        return 'T'
    elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
        return 'V'
    elif codon == 'UGG':
        return 'W'
    elif codon == 'UAU' or codon == 'UAC':
        return 'Y'
    else:
        return "invalid codon"
