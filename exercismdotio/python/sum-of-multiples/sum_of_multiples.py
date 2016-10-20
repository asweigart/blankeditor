def sum_of_multiples(maxNum, multiples):
	multiplesToSum = []

	for index, multiple in enumerate(multiples): # loop through each multiple
		if multiple == 0:
			continue

		for number in range(0, maxNum): # loop through each number, testing if it is a multiple of `multiple`
			if number % multiple == 0:
				multiplesToSum.append(number)
	
	return sum(set(multiplesToSum))