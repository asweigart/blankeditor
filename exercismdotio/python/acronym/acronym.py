import re


def abbreviate(stringToAcronymize):
	completeAcronym = []

	for wordPart in re.split('\s|-', stringToAcronymize):
		if wordPart.isupper():
			completeAcronym.append(wordPart[0])
		else:
			completeAcronym.extend(abbreviateHelper(wordPart))

	return ''.join(completeAcronym)

def abbreviateHelper(stringToAcronymize):
	isStartOfWord = True

	acronymToReturn = []
	for symbol in stringToAcronymize:
		# handle uppercase letters
		if symbol.isupper():
			acronymToReturn.append(symbol)
			isStartOfWord = False
			continue

		# set isStartOfWord
		if symbol == ' ' or symbol == '-':
			isStartOfWord = True
			continue

		# handle first letters of words
		if isStartOfWord and symbol.isalpha():
			acronymToReturn.append(symbol.upper())
			isStartOfWord = False

	return ''.join(acronymToReturn)