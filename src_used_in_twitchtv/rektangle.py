# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/
import logging
logging.basicConfig(level=logging.DEBUG)

def getRow(word, width, startReversed):
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
		theRow[index] = wordInRow[1:]
		logging.debug('After: %s' % (theRow[index]))

	return ' '.join(theRow)

def displayRektangle(word, width, height):
	# print out row. (even rows are forwards, odd rows are backwards)
	for row in range(height + 1):
		if row % 2 == 0:
			print(getRow())
		else:
			print(getRow())

print(getRow('REKT', 1, False))
print(getRow('REKT', 1, True))
print(getRow('REKT', 2, False))
print(getRow('REKT', 2, True))
print(getRow('REKT', 3, False))
print(getRow('REKT', 3, True))


displayRektangle('REKT', 1, 1)
print()
displayRektangle('REKT', 2, 1)
print()
displayRektangle('REKT', 2, 2)