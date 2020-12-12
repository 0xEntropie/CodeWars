def DNA_strand(dna):

    dict = {'A':'T','T':'A','G':'C','C':'G'}
    DNA_strand = ''
    for x in dna: DNA_strand +=dict[x] 
    return DNA_strand
