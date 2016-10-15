def distance(s1, s2):
	# Returns the hamming distance between strings `s1` and `s21`
	hammingDistance = 0
	for index in range(len(min(s1, s2))):
		if s1[index] != s2[index]:
			hammingDistance += 1

	return hammingDistance + abs(len(s1) - len(s2))