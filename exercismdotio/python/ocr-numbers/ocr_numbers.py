def number(numbers):
	if len(numbers) != 4: 
		raise ValueError
		
	# validation checks
	for index, line in enumerate(numbers):
		if len(line) % 3 != 0:
			raise ValueError('Line is the wrong size')

		if len(line) != len(numbers[0]):
			raise ValueError()

	identifiedNumbers = []
	for index in range(0, len(numbers[0]), 3):
		identifiedNumbers.append(identifyDigit([numbers[0][index:index+3], 
												numbers[1][index:index+3], 
												numbers[2][index:index+3],
												numbers[3][index:index+3]]))
	return ''.join(identifiedNumbers)



def grid(numbers):
	generatedNumber = [[], [], [], []]
	for digit in numbers:
		genDigit = generateDigit(digit)
		generatedNumber[0].extend(genDigit[0])
		generatedNumber[1].extend(genDigit[1])
		generatedNumber[2].extend(genDigit[2])
		generatedNumber[3].extend(genDigit[3])

	generatedNumber[0] = ''.join(generatedNumber[0])
	generatedNumber[1] = ''.join(generatedNumber[1])
	generatedNumber[2] = ''.join(generatedNumber[2])
	generatedNumber[3] = ''.join(generatedNumber[3])

	return generatedNumber


def identifyDigit(digit):
	if digit == [' _ ', '| |', '|_|', '   ']:
		return '0'
	elif digit == ['   ', '  |', '  |', '   ']:
		return '1'
	elif digit == [' _ ', ' _|', '|_ ', '   ']:
		return '2'
	elif digit == [' _ ', ' _|', ' _|', '   ']:
		return '3'
	elif digit == ['   ', '|_|', '  |', '   ']:
		return '4'
	elif digit == [' _ ', '|_ ', ' _|', '   ']:
		return '5'
	elif digit == [' _ ', '|_ ', '|_|', '   ']:
		return '6'
	elif digit == [' _ ', '  |', '  |', '   ']:
		return '7'
	elif digit == [' _ ', '|_|', '|_|', '   ']:
		return '8'
	elif digit == [' _ ', '|_|', ' _|', '   ']:
		return '9'
	else:
		return '?'

def generateDigit(digit):
	if digit == '0':
		return [' _ ', '| |', '|_|', '   ']
	elif digit == '1': 
		return ['   ', '  |', '  |', '   ']
	elif digit == '2':
		return [' _ ', ' _|', '|_ ', '   ']
	elif digit == '3':
		return [' _ ', ' _|', ' _|', '   ']
	elif digit == '4':
		return ['   ', '|_|', '  |', '   ']
	elif digit == '5':
		return [' _ ', '|_ ', ' _|', '   ']
	elif digit == '6':
		return [' _ ', '|_ ', '|_|', '   ']
	elif digit == '7':
		return [' _ ', '  |', '  |', '   ']
	elif digit == '8':
		return [' _ ', '|_|', '|_|', '   ']
	elif digit == '9':
		return [' _ ', '|_|', ' _|', '   ']
	else:
		raise ValueError
