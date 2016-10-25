import doctest

def say(number):
	number = int(number)

	if number < 0 or number >= 1000000000000:
		raise AttributeError

	if number == 0:
		return 'zero'
	elif number >= 1000000000:
		return sayBillions(number)
	elif number >= 1000000:
		return sayMillions(number)
	elif number >= 1000:
		return sayThousands(number)
	else:
		return sayHundredsTensOnes(number)

	return 


def handleLastThreeDigits(lastThreeDigits):
	numberStr = ''
	if lastThreeDigits != 0:
		if lastThreeDigits < 100:
			numberStr += ' and ' + sayHundredsTensOnes(lastThreeDigits)
		else:
			numberStr += ' ' + sayHundredsTensOnes(lastThreeDigits)
	return numberStr


def sayBillions(number):
	assert 1000000000 <= number < 1000000000000, 'Passed in ' + str(number)

	billionsThreeDigits = int(str(number)[0:-9])
	millionsThreeDigits = int(str(number)[-9:-6])
	thousandsThreeDigits = int(str(number)[-6:-3])
	lastThreeDigits = int(str(number)[-3:])

	numberStr = sayHundredsTensOnes(billionsThreeDigits) + ' billion'

	if millionsThreeDigits != 0:
		numberStr += ' ' + sayHundredsTensOnes(millionsThreeDigits) + ' million'

	if thousandsThreeDigits != 0:
		numberStr += ' ' + sayHundredsTensOnes(thousandsThreeDigits) + ' thousand'

	numberStr += handleLastThreeDigits(lastThreeDigits)

	return numberStr


def sayMillions(number):
	"""
	>>> sayMillions(123456789)
	'one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine'
	"""
	assert 1000000 <= number < 1000000000, 'Passed in ' + str(number)

	millionsThreeDigits = int(str(number)[0:-6])
	thousandsThreeDigits = int(str(number)[-6:-3])
	lastThreeDigits = int(str(number)[-3:])

	numberStr = sayHundredsTensOnes(millionsThreeDigits) + ' million'

	if thousandsThreeDigits != 0:
		numberStr += ' ' + sayHundredsTensOnes(thousandsThreeDigits) + ' thousand'

	numberStr += handleLastThreeDigits(lastThreeDigits)

	return numberStr

def sayThousands(number):
	"""
	>>> sayThousands(1000)
	'one thousand'
	>>> sayThousands(1001)
	'one thousand and one'
	>>> sayThousands(999999)
	'nine hundred and ninety-nine thousand nine hundred and ninety-nine'
	"""
	assert 1000 <= number < 1000000, 'Passed in ' + str(number)

	thousandsThreeDigits = int(str(number)[0:-3])
	lastThreeDigits = int(str(number)[-3:])

	numberStr = sayHundredsTensOnes(thousandsThreeDigits) + ' thousand'

	numberStr += handleLastThreeDigits(lastThreeDigits)	

	return numberStr

def sayHundredsTensOnes(number):
	numberStr = ''
	if 100 <= number < 1000:
		numberStr += sayHundreds(number)
	elif 10 <= number < 100:
		numberStr += sayTens(number)
	elif 1 <= number < 10:
		numberStr += sayOnes(number)	
	return numberStr

def sayHundreds(number):
	"""
	>>> sayHundreds(926)
	'nine hundred and twenty-six'
	"""
	assert 100 <= number < 1000, 'Passed in ' + str(number)

	numberStr = sayOnes(int(str(number)[0])) + ' hundred'
	if int(str(number)[1:3]) != 0:
		numberStr += ' and ' + sayTens(int(str(number)[1:3]))

	return numberStr

def sayTens(number):
	"""
	>>> sayTens(10)
	'ten'
	>>> sayTens(20)
	'twenty'
	>>> sayTens(21)
	'twenty-one'
	"""
	assert 10 <= number < 100, 'Passed in ' + str(number)

	if 10 <= number <= 19:
		return {10: 'ten',
				11: 'eleven',
				12: 'twelve',
				13: 'thirteen',
				14: 'fourteen',
				15: 'fifteen',
				16: 'sixteen',
				17: 'seventeen',
				18: 'eighteen',
				19: 'nineteen'}[number]

	numberStr = {2: 'twenty',
 				 3: 'thirty',
 				 4: 'forty',
 				 5: 'fifty',
 				 6: 'sixty',
				 7: 'seventy',
				 8: 'eighty',
				 9: 'ninety'}[int(str(number)[0])] 

	if int(str(number)[1]) != 0:
		numberStr += '-' + sayOnes(int(str(number)[1]))

	return numberStr




def sayOnes(number):
	assert 0 <= number < 10
	return {0: '',
			1: 'one',
			2: 'two',
			3: 'three',
			4: 'four',
			5: 'five',
			6: 'six',
			7: 'seven',
			8: 'eight',
			9: 'nine'}[number]

doctest.testmod()			