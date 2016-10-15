def to_rna(nucleotides):
	rnaNucleotides = []

	for letter in nucleotides:
		if letter == 'A':
			rnaNucleotides.append('U')
		elif letter == 'T':
			rnaNucleotides.append('A')
		elif letter == 'C':
			rnaNucleotides.append('G')
		elif letter == 'G':
			rnaNucleotides.append('C')

	return ''.join(rnaNucleotides)