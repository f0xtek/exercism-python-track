def proteins(strand):
    rns_codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    protein_list = []
    proteins_codons = {
        'Methionine': ['AUG'],
        'Phenylalanine': ['UUU', 'UUC'],
        'Leucine': ['UUA', 'UUG'],
        'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
        'Tyrosine': ['UAU', 'UAC'],
        'Cysteine': ['UGU', 'UGC'],
        'Tryptophan': ['UGG']
    }
    stop_codons = ['UAA', 'UAG', 'UGA']

    for rns in rns_codons:
        for protein, codons in proteins_codons.items():
            if rns in stop_codons:
                return protein_list
            elif rns in codons:
                protein_list.append(protein)

    return protein_list
