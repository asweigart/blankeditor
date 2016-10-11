import math
import logging
logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)

SIEVE_SIZE = 2000000

# generate the sieve
sieveOfPrimes = [True] * (SIEVE_SIZE+1)
sieveOfPrimes[0] = False

for num1 in range(2, SIEVE_SIZE):
	i = num1 * 2
	while i < SIEVE_SIZE:
		sieveOfPrimes[i] = False
		i += num1


def isPrime(theNumber):
	return sieveOfPrimes[theNumber]

primes = []
for num in range(2, SIEVE_SIZE):
	if isPrime(num):
		primes.append(num)
print(sum(primes))


#for i in range(1999000, 2000001):
#	print(i, sieveOfPrimes[i])