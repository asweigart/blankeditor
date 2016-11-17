class Phone():
	def __init__(self, rawPhoneNumber):
		# pulling out non-digits without regular expressions:
		cleanedUpPhoneNumber = []
		for character in rawPhoneNumber:
			if character in '1234567890':
				cleanedUpPhoneNumber.append(character)
		cleanedUpPhoneNumber = ''.join(cleanedUpPhoneNumber)

		# check that this is a logical phone number
		if len(cleanedUpPhoneNumber) == 10:
			self.number = cleanedUpPhoneNumber
		elif len(cleanedUpPhoneNumber) == 11 and cleanedUpPhoneNumber[0] == '1':
			self.number = cleanedUpPhoneNumber[1:]
		else:
			self.number = '0000000000'

	def area_code(self):
		return self.number[:3]

	def pretty(self):
		return '(%s) %s-%s' % (self.number[:3], self.number[3:6], self.number[6:])
		
