import doctest
import logging
logging.basicConfig(level=logging.DEBUG)


def encode(uncompressedStr):
	compressedStr = []

	currentRunLength = 0
	currentRunLetter = uncompressedStr[0]

	for letter in uncompressedStr: #  'AABBBCCCC'
		if letter == currentRunLetter:
			currentRunLength += 1
		else:
			if currentRunLength > 1:
				compressedStr.append(str(currentRunLength) + currentRunLetter)
			else:
				compressedStr.append(currentRunLetter)
			currentRunLetter = letter
			currentRunLength = 1

	if currentRunLength > 1:
		compressedStr.append(str(currentRunLength) + currentRunLetter)
	else:
		compressedStr.append(currentRunLetter)
	
	return ''.join(compressedStr)

def splitNumbersAndLetters(theString):
	"""
	>>> splitNumbersAndLetters('12A4B')
	['12', 'A', '4', 'B']
	>>> splitNumbersAndLetters('12A4BC')
	['12', 'A', '4', 'B', '1', C']
	>>> splitNumbersAndLetters('ABC')
	['1', 'A', '1', 'B', '1', 'C']
	"""
	splitList = []

	if not theString[0].isdigit():
		mode = 'nondigits'
	else:
		mode = 'digits'

	currentRunLength = 0
	for index, character in enumerate(theString):
		if (mode == 'nondigits' and character.isdigit()) or (mode == 'digits' and not character.isdigit()):
			# there's been a change in mode
			splitList.append(theString[index-currentRunLength:index])
			if mode == 'nondigits':
				mode = 'digits'
			elif mode == 'digits':
				mode = 'nondigits'
			else:
				assert False

			currentRunLength = 1
		else:
			# there's been no change in mode
			currentRunLength += 1

	splitList.append(theString[index-currentRunLength+1:])
	return splitList

def decode(compressedStr):

	return


doctest.testmod()