class Luhn():
	def __init__(self, number):
		self.number = number

	def addends(self):
		result = []

		doubleTheDigit = False
		for i in reversed(str(self.number)):
			if doubleTheDigit:
				resultNumber = int(i) * 2
				if resultNumber > 10:
					resultNumber -= 9
				result.append(resultNumber)
			else:
				result.append(int(i))

			doubleTheDigit = not doubleTheDigit

		return result

	def checksum(self):
		return sum(self.addends())

	def is_valid(self):
		return self.checksum() % 10 == 0

	@staticmethod
	def create(number):
		for i in range(0, 10):
			testNumber = number * 10 + i
			if Luhn(testNumber).is_valid():
				return testNumber

		assert False