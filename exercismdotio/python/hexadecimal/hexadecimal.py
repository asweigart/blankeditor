def hexa(number):
	number = number.lower()
	for index, value in enumerate(number):
		if value not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'):
			raise ValueError()

	digitMapping = {'5': 5, '7': 7, '0': 0, '1': 1, '6': 6, '2': 2, '8': 8, '3': 3, '9': 9, '4': 4, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

	decimalNumber = 0
	for digitIndex in range(-1, -len(number) - 1, -1):
		digitValue = digitMapping[number[digitIndex]]
		decimalNumber += digitValue * (16 ** (-digitIndex - 1))
	return decimalNumber