def numeral(number):
	romanNumeral = ''

	if number >= 1000:
		thousandsPlace = (number - (number % 1000)) // 1000
		romanNumeral += romanThousandsPlace(thousandsPlace)
		number = number % 1000
	if number >= 100:
		hundredsPlace = (number - (number % 100)) // 100
		romanNumeral += romanHundredsPlace(hundredsPlace)
		number = number % 100
	if number >= 10:
		tensPlace = (number - (number % 10)) // 10
		romanNumeral += romanTensPlace(tensPlace)
		number = number % 10
	if number >= 1:
		#onesPlace = (number - (number % 1)) // 1
		romanNumeral += romanOnesPlace(number)
		#number = number % 10

	return romanNumeral


def romanOnesPlace(number):
	assert len(str(number)) == 1

	return {1: 'I', 
			2: 'II',
			3: 'III',
			4: 'IV',
			5: 'V',
			6: 'VI',
			7: 'VII',
			8: 'VIII',
			9: 'IX'}[number]

def romanTensPlace(number):
	assert len(str(number)) == 1

	return {1: 'X', 
			2: 'XX',
			3: 'XXX',
			4: 'XL',
			5: 'L',
			6: 'LX',
			7: 'LXX',
			8: 'LXXX',
			9: 'XC'}[number]	

def romanHundredsPlace(number):
	assert len(str(number)) == 1

	return {1: 'C', 
			2: 'CC',
			3: 'CCC',
			4: 'CD',
			5: 'D',
			6: 'DC',
			7: 'DCC',
			8: 'DCCC',
			9: 'CM'}[number]

def romanThousandsPlace(number):
	assert len(str(number)) == 1


	return {1: 'M', 
			2: 'MM',
			3: 'MMM'}[number]