import math


def primitive_triplets(b):
	if b % 4 != 0:
		raise ValueError()

def triplets_in_range(minNum, maxNum):
	pass


def is_triplet(triplet):
	a, b, c = triplet 
	return a**2 + b**2 == c**2



def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def getFactorsOf(number):
	factors = [(1, number)]
	for i in range(2, int(math.sqrt(number))):
		if number % i == 0:
			factors.append( (i, number // i) )
	return factors