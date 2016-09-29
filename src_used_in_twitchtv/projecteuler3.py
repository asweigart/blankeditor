import logging
import math
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def getFactors(theNumber):
	factors = []
	for number in range(1, int(math.sqrt(theNumber) + 1)):
		if theNumber % number == 0:
			factors.append(number)
			factors.append(theNumber // number)
	return factors

def isPrime(theNumber):
	return len(getFactors(theNumber)) == 2

logging.debug(getFactors(600851475143))

allFactors = getFactors(600851475143)
logging.debug(str(allFactors))

largestPrimeFactor = 0
for factor in allFactors:
	if isPrime(factor) and factor > largestPrimeFactor:
		largestPrimeFactor = factor
		logging.debug('new largest prime factor: ' + str(factor))

print(largestPrimeFactor)
