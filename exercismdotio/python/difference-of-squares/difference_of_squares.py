
def difference(maxLimit):
	return square_of_sum(maxLimit) - sum_of_squares(maxLimit)


def square_of_sum(maxLimit):
	# squareOfSums == (1 + 2 + 3 + 4 ...) ** 2
	squareOfSums = 0
	for num in range(1, maxLimit + 1):
		squareOfSums += num
	squareOfSums = squareOfSums ** 2
	return squareOfSums


def sum_of_squares(maxLimit):
	# sumOfSquares == 1*1 + 2*2 + 3*3

	sumOfSquares = 0
	for num in range(1, maxLimit + 1):
		sumOfSquares += (num * num)
	return sumOfSquares






