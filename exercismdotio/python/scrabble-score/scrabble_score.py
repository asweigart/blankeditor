POINT_VALUE = {'k': 5, 'e': 1, 'a': 1, 'm': 3, 'y': 4, 'u': 1, 'w': 4, 'v': 4, 'b': 3, 'n': 1, 'j': 8, 'f': 4, 's': 1, 'g': 2, 'z': 10, 'h': 4, 'l': 1, 't': 1, 'i': 1, 'x': 8, 'p': 3, 'r': 1, 'o': 1, 'd': 2, 'q': 10, 'c': 3}


def score(word):
	if not word.isalpha():
		return 0

	word = word.lower()

	total = 0
	for letter in word:
		total += POINT_VALUE[letter]

	return total