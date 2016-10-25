def largest_product(number, digits):
	# `digits` which would be negative or bigger than `number` is invalid
	if digits > len(number) or digits < 0:
		raise ValueError

	# if `digits` is 0, always return 1 (for some reason, this is what the unit tests want)
	if digits == 0:
		return 1

	# raise ValueError if `number` is an invalid number
	int(number)

	# track the largest product we've found
	largestProductSoFar = 0

	# starting index is the first of the `digits`-digits that we want to multiply
	for startingIndex in range(len(number) - digits + 1):
		product = 1

		# `startingIndex` + `addIndex` is the index of the next digit to multiply
		for addIndex in range(digits):
			product *= int(number[startingIndex + addIndex])

		# update `largestProductSoFar` if the product is larger
		if product > largestProductSoFar:
			largestProductSoFar = product

	return largestProductSoFar