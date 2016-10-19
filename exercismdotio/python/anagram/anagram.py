import doctest

def getLetterCount(word):
	# get letter counts of word1 and word2 in a dictionary, like this: {'a': 0, 'b': 2, ...}
	letterCount = {}
	for letter in word.lower():
		letterCount.setdefault(letter, 0)
		letterCount[letter] += 1
	return letterCount



def isAnagram(word1, word2):
	return getLetterCount(word1) == getLetterCount(word2) and word1.lower() != word2.lower()


def detect_anagrams(originalWord, possibleAnagrams):
	allAnagrams = []
	for possibleAnagram in possibleAnagrams:
		if isAnagram(originalWord, possibleAnagram):
			allAnagrams.append(possibleAnagram)

	return allAnagrams

doctest.testmod()	