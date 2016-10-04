# https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/
import doctest
import logging
logging.basicConfig(level=logging.DEBUG)

def getReverseFactorial(number):
	'''
	>>> getReverseFactorial(120)
	5
	>>> getReverseFactorial(150)
	>>> getReverseFactorial(720)
	6
	>>> getReverseFactorial(3628800)
	10
	>>> getReverseFactorial(479001600)
	12
	>>> getReverseFactorial(6)
	3
	>>> getReverseFactorial(18)
	'''
	factorialResult = 1
	multiplyBy = 1
	while factorialResult <= number:
		factorialResult *= multiplyBy   # factorialResult will be equal to "multipleBy!""
		logging.debug('factorialResult = %s, multiplyBy = %s' % (factorialResult, multiplyBy))
		if factorialResult == number:
			return multiplyBy
		multiplyBy += 1
	return None

doctest.testmod()