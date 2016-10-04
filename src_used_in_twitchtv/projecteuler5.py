import doctest
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def isEvenlyDivisible1to20(number):
	'''
	>>> isEvenlyDivisible1to20(123)
	False
	>>> isEvenlyDivisible1to20(2432902008176640000)
	True
	'''
	for modBy in range(1, 21):
		if number % modBy != 0:
			return False
	return True

testNumber = 20
while True:
	if testNumber % 1000000 == 0:
		logging.debug('testNumber: %s' % testNumber)
	if isEvenlyDivisible1to20(testNumber):
		print(testNumber)
		break
	testNumber += 20

doctest.testmod()