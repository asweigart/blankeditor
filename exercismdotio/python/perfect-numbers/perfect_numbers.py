import math
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def is_perfect(number):
	factors = [1]

	for divisor in range(2, int(math.sqrt(number)) + 1):
		if number % divisor == 0:
			factors.append(divisor)
			factors.append(number // divisor)
	factors = set(factors)
	logging.debug(factors)
	logging.debug(sum(factors))

	return number == sum(factors)