# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/
import logging
import doctest
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def getRow(word, width, startReversed):
	"""
	>>> getRow('REKT', 1, False)
	'R E K T'
	>>> getRow('REKT', 1, True)
	'T K E R'
	>>> getRow('REKT', 2, False)
	'R E K T K E R'
	>>> getRow('REKT', 2, True)
	'T K E R E K T'
	>>> getRow('REKT', 3, False)
	'R E K T K E R E K T'
	>>> getRow('REKT', 3, True)
	'T K E R E K T K E R'
	"""
	#if width % 2 == 0:
	#	startReversed = not startReversed

	theRow = []
	for i in range(width):
		if not startReversed:
			theRow.append(' '.join(word))
		else:
			theRow.append(' '.join(word[::-1]))
		startReversed = not startReversed

	logging.debug('theRow: %s' % (theRow))

	for index, wordInRow in enumerate(theRow):
		if index == 0: continue

		logging.debug('%s %s' % (wordInRow, wordInRow[1:]))
		logging.debug('Before: %s' % (theRow[index]))
		theRow[index] = wordInRow[2:]
		logging.debug('After: %s' % (theRow[index]))

	return ' '.join(theRow)

def getInBetweenRows(word, width, wordIndex):
	'''
	>>> getInBetweenRows('REKT', 1, 1)
	'E     K'
	>>> getInBetweenRows('REKT', 1, 2)
	'K     E'
	>>> getInBetweenRows('REKT', 2, 1)
	'E     K     E'
	>>> getInBetweenRows('REKT', 2, 2)
	'K     E     K'
	>>> getInBetweenRows('REKTANGLE', 1, 5)
	'N               T'
	'''
	letter = word[wordIndex]
	altLetter = word[-(wordIndex + 1)]

	theRow = []
	appendAlt = False
	for i in range(width + 1):
		if not appendAlt:
			theRow.append(letter)
		else:
			theRow.append(altLetter)
		appendAlt = not appendAlt
	spacesInBetweenEachLetter = (' ' * (((len(word) - 2) * 2) + 1))
	return spacesInBetweenEachLetter.join(theRow)


def displayRektangle(word, width, height):
	if width % 2 == 0:
		startReversed = True
	else:
		startReversed = False

	# print out row. (even rows are forwards, odd rows are backwards)
	for rowNumber in range(height):
		# print the entire row from getRow()
		print(getRow(word, width, startReversed))


		# print the in between rows from getInBetweenRows()
		for inBetweenRowNumber in range(1, len(word) - 1):
			if startReversed:
				print(getInBetweenRows(word, width, len(word) - inBetweenRowNumber))
			else:
				print(getInBetweenRows(word, width, inBetweenRowNumber))


		startReversed = not startReversed

	print(getRow(word, width, startReversed))


doctest.testmod()

displayRektangle('REKT', 1, 1)
print()
displayRektangle('REKT', 2, 1)
print()
displayRektangle('REKT', 2, 2)
