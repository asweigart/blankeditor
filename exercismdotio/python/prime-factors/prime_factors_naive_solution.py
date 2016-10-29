import logging, math
logging.basicConfig(level=logging.DEBUG)

logging.disable(logging.CRITICAL)

def isPrime(number):
	for possibleFactor in range(2, math.sqrt(number) + 1):
		if number % possibleFactor == 0:
			return False
	return True


def prime_factors(number):
	if number == 1:
		return []


	primeFactors = []
	numbersToFactor = [number] # starts as `number`, and holds the numbers we need to factor and test for primality

	# as long as we have numbers to factor, keep factoring them
	while len(numbersToFactor) > 0:
		logging.debug('numbersToFactor == %s' % (numbersToFactor))
		logging.debug('primeFactors == %s\n\n' % (primeFactors))

		numberToTest = numbersToFactor.pop()

		if isPrime(numberToTest):
			# primes always get added `primeFactors`
			primeFactors.append(numberToTest)
		else:
			# if it's not prime, find factors of it
			for possibleFactor in range(2, math.sqrt(numberToTest) + 1):
				if numberToTest % possibleFactor == 0:
					# factors of `numberToTest` found

					# prime factors get appended to `primeFactors`
					# non prime factors get appended to `numbersToFactor`
					if isPrime(possibleFactor):
						primeFactors.append(possibleFactor)
					else:
						numbersToFactor.append(possibleFactor)


					if isPrime(numberToTest // possibleFactor):
						primeFactors.append(numberToTest // possibleFactor)
					else:
						numbersToFactor.append(numberToTest // possibleFactor)
					break


	primeFactors.sort()
	return primeFactors