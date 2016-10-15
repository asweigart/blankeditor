import collections

def word_count(sentence):
	sentence = sentence.lower()

	# remove non-letters/spaces
	onlyLettersSpaces = []
	for character in sentence:
		if character.isalpha() or character.isspace() or character.isdigit():
			onlyLettersSpaces.append(character)
		else:
			onlyLettersSpaces.append(' ')
	onlyLettersSpaces = ''.join(onlyLettersSpaces)

	words = onlyLettersSpaces.split()

	wordCount = dict(collections.Counter(words))

	return wordCount
