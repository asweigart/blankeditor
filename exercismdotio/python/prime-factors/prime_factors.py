import logging, math
logging.basicConfig(level=logging.DEBUG)

logging.disable(logging.CRITICAL)

LOW_PRIMES = lowPrimes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997}

def isPrime(number):
	if number in LOW_PRIMES:
		return True

	for possibleFactor in range(2, int(math.sqrt(number)) + 1):
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

			for possibleFactor in range(2, int(math.sqrt(numberToTest)) + 1):
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