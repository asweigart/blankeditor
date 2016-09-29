
sumOfMultiples = 0

# go through all numbers 1 to 1000
for number in range(1, 1000):

# find out if multiple of 3 or 5
	if (number % 3 == 0) or (number % 5 == 0):
		# find the sum of the multiples
		sumOfMultiples += number

print(sumOfMultiples)