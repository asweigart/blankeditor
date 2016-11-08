import logging
logging.basicConfig()

def saddle_points(matrix):
	if len(matrix) == 0:
		return set()

	# check that the matrix is regular
	firstRowLen = len(matrix[0])
	for row in matrix:
		if len(row) != firstRowLen:
			raise ValueError('The matrix is irregular.')

	# check each number in the matrix for saddle-pointedness
	saddlePoints = []
	for rowIndex, row in enumerate(matrix):
		for columnIndex in range(len(row)):
			possibleSaddle = matrix[rowIndex][columnIndex]

			# check if the possible saddle is >= than any other number in the row:
			if possibleSaddle < max(row):
				continue

			# check if the possible saddle is <= than anyo ther number in the column:
			column = []
			for rowIndex2 in range(len(matrix)):
				column.append(matrix[rowIndex2][columnIndex])
			if possibleSaddle <= min(column):
				# this is a saddle point
				saddlePoints.append((rowIndex, columnIndex))

	return set(saddlePoints)