import logging
logging.basicConfig(level=logging.DEBUG)

def sieve(maxNum):
	isPrime = [True] * (maxNum + 1)

	isPrime[0] = False
	isPrime[1] = False

	for startingIndex in range(2, maxNum + 1):
		pointer = startingIndex

		while pointer + startingIndex <= maxNum:
			pointer += startingIndex
			isPrime[pointer] = False
		logging.debug(startingIndex, isPrime)

	primes = []
	for index, isPrimeNum in enumerate(isPrime):
		if isPrimeNum:
			primes.append(index)

	return primes