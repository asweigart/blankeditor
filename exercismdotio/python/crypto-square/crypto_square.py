import re, math, logging

logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def encode(plaintext):
	# normalize the plaintext
	plaintext = plaintext.lower()
	notLowercaseRegex = re.compile(r'[^a-z0-9]')
	plaintext = notLowercaseRegex.sub('', plaintext)

	# figure out how many rows and columns we need
	rows = int(math.sqrt(len(plaintext)))
	columns = rows

	if not int(math.sqrt(len(plaintext))) == math.sqrt(len(plaintext)):
		columns += 1
	logging.debug('rows == %s, columns == %s' % (rows, columns))

	square = {}
	columnPointer = 0
	rowPointer = 0
	for index, letter in enumerate(plaintext):
		square[(columnPointer, rowPointer)] = letter
		columnPointer += 1
		if columnPointer == columns:
			columnPointer = 0
			rowPointer += 1

	logging.debug(square)

	ciphertext = ''
	for x in range(columns):
		for y in range(rows):
			try:
				ciphertext += square[(x, y)]
			except KeyError:
				pass
		ciphertext += ' '

	return ciphertext.strip()




def decode(plaintext):
	# normalize the plaintext
	plaintext = plaintext.lower()
	notLowercaseRegex = re.compile(r'[^a-z0-9]')
	plaintext = notLowercaseRegex.sub('', plaintext)

	# figure out how many rows and columns we need
	rows = int(math.sqrt(len(plaintext)))
	columns = rows

	if not int(math.sqrt(len(plaintext))) == math.sqrt(len(plaintext)):
		columns += 1

	rows, columns = columns, rows
	logging.debug('rows == %s, columns == %s' % (rows, columns))


	numEmptySpaces = rows * columns - len(plaintext)

	square = {}

	
	columnPointer = 0
	rowPointer = 0
	for index, letter in enumerate(plaintext):
		if columnPointer == columns - 1 and rowPointer >= rows - numEmptySpaces:
			columnPointer = 0
			rowPointer += 1
		
		square[(columnPointer, rowPointer)] = letter

		columnPointer += 1
		if columnPointer == columns:
			columnPointer = 0
			rowPointer += 1
	
	logging.debug(square)


	ciphertext = ''
	for x in range(columns):
		for y in range(rows):
			if x == columns - 1 and y == rows - numEmptySpaces:
				return ciphertext
			ciphertext += square[(x, y)]

		ciphertext += ' '
