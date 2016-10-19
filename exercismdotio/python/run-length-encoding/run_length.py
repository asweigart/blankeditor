import doctest
import logging
import re
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
	['12', 'A', '4', 'B', '1', 'C']
	>>> splitNumbersAndLetters('ABC')
	['1', 'A', '1', 'B', '1', 'C']
	"""
	pat = re.compile(r'(\d+|\D)')
	splitList = pat.findall(theString)

	# insert any missing '1' strings
	expectingNumber = True
	index = 0
	while index < len(splitList):
		if expectingNumber and not splitList[index].isdigit():
			splitList.insert(index, '1')
		expectingNumber = not expectingNumber
		index += 1
	return splitList

def decode(compressedStr):
	"""
	>>> decode('12A4B')
	'AAAAAAAAAAAABBBB'
	"""
	splitList = splitNumbersAndLetters(compressedStr)

	uncompressedStr = []
	for index in range(0, len(splitList), 2):
		uncompressedStr.append( int(splitList[index]) * splitList[index + 1] )
	
	return ''.join(uncompressedStr)


doctest.testmod()