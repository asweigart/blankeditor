import math
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def primitive_triplets(b):
	if b % 4 != 0:
		raise ValueError()

	results = []
	all_m_n = getPythagFactorsOf(b // 2)
	for m, n in all_m_n:
		a = m**2 - n**2
		c = m**2 + n**2

		#if not (gcd(a, b) == 1 and gcd(b, c) == 1):
		#	continue

		if a > b:
			results.append( (b, a, c) )
		else:
			results.append( (a, b, c) )
	return set(results)

def triplets_in_range(minNum, maxNum):
	# gets all primitive triplets
	triplets = []
	for b in range(1, maxNum + 1):
		if b % 4 == 0:
			triplets.extend(primitive_triplets(b))

	logging.debug(triplets)

	# find all multiples of a/b/c that are still in range
	tripletMultiples = []
	for triplet in triplets:
		a, b, c = triplet
		multiplyBy = 2
		while c * multiplyBy <= maxNum:
			tripletMultiples.append( (a * multiplyBy, b * multiplyBy, c * multiplyBy) )
			multiplyBy += 1
	triplets.extend(tripletMultiples)

	logging.debug(triplets)

	# get rid of any triplets that have a < minNum or c > maxNum
	for index in range(len(triplets) - 1, -1, -1):
		if triplets[index][0] < minNum or triplets[index][2] > maxNum:
			del triplets[index]

	logging.debug(triplets)
	return set(triplets)



def is_triplet(triplet):
	a, b, c = sorted(list(triplet))
	return a**2 + b**2 == c**2



def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def getPythagFactorsOf(number):
	'''Return all factors of `number` as a list of two-integer tuples.
	The two integers are m and n, where m > n and m and n are coprime'''
	factors = [(number, 1)]
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0 and gcd(number // i, i) == 1 and (number // i - i) % 2 == 1:
			if i > number // i:
				factors.append( (i, number // i) )
			else:
				factors.append( (number // i, i) )
	return factors