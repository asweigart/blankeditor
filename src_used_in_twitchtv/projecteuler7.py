import doctest
import math
import logging
logging.basicConfig(level=logging.DEBUG)

def isPrime(number):
	'''
	>>> isPrime(3)
	True
	>>> isPrime(7)
	True
	>>> isPrime(13)
	True
	>>> isPrime(21)
	False
	>>> isPrime(10)
	False
	'''
	for modBy in range(2, int(math.sqrt(number)) + 1):
		if number % modBy == 0:
			# modBy is a factor of number, therefore number is not prime
			return False
	return True

primesFound = 0
number = 1
while primesFound < 10001:
	number += 1
	if isPrime(number):
		primesFound += 1

	
print(number)

doctest.testmod()