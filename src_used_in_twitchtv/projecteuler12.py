import doctest, math, logging

logging.basicConfig(level=logging.DEBUG)

def getTriangularNumber(num):
	"""Returns the triangular number of `num`

	>>> getTriangularNumber(1)
	1
	>>> getTriangularNumber(2)
	3
	>>> getTriangularNumber(7)
	28
	"""
	total = 0
	for i in range(1, num + 1):
		total += i
	return total



def getFactors(num):
	"""Returns a list of factors of `num`.
	>>> getFactors(1)
	[1]
	>>> getFactors(6)
	[1, 2, 3, 6]
	>>> getFactors(28)
	[1, 2, 4, 7, 14, 28]
	"""
	factors = [1, num]
	for possibleFactor in range(2, int(math.sqrt(num)) + 1):
		if num % possibleFactor == 0:
			factors.append(possibleFactor)
			factors.append(num // possibleFactor)
			#logging.debug('new factors of %s found: %s %s' % (num, factors[-1], factors[-2]))

	factors = list(set(factors)) # get rid of duplicate values
	factors.sort()
	return factors
	

doctest.testmod()


i = 1
while True:
	triangularNum = getTriangularNumber(i)
	factorsOfTriNum = getFactors(triangularNum)
	if len(factorsOfTriNum) > 500:
		break

	i += 1

print(triangularNum)	
