

def parse_binary(number):
	for index, value in enumerate(number):
		if value not in ('0', '1'):
			raise ValueError()

	decimalNumber = 0
	for digitIndex in range(-1, -len(number) - 1, -1):
		decimalNumber += int(number[digitIndex]) * (2 ** (-digitIndex - 1))
	return decimalNumber