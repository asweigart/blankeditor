import copy

def board(board):
	# check that the board is formatted correctly.
	firstLine = board[0]
	if '+' + ('-' * (len(firstLine) - 2)) + '+' != firstLine:
		raise ValueError('First line is not valid')

	lastLine = board[-1]
	if '+' + ('-' * (len(lastLine) - 2)) + '+' != lastLine:
		raise ValueError('Last line is not valid')
	
	for line in board:
		if len(line) != len(board[0]):
			raise ValueError('Board is not a rectangle.')

	# turn numberedBoard into a list of lists of strings
	numberedBoard = copy.copy(board)
	for index in range(len(numberedBoard)):
		numberedBoard[index] = list(numberedBoard[index])


	# number the mines
	for boardIndex, line in enumerate(board):
		# skip the first and last border lines
		if boardIndex == 0 or boardIndex == len(board) - 1:
			continue

		if line[0] != '|' or line[-1] != '|':
			raise ValueError('Missing pipe character')

		for lineIndex, spaceOrMine in enumerate(line):
			if lineIndex == 0 or lineIndex == len(line) - 1:
				continue 

			if spaceOrMine not in (' ', '*'):
				raise ValueError('Invalid board character')

			if spaceOrMine == '*':
				# found a mine, add 1 to adjacent spaces

				for x in range(-1, 2):
					for y in range(-1, 2):
						if numberedBoard[boardIndex + y][lineIndex + x] == ' ':
							numberedBoard[boardIndex + y][lineIndex + x] = '1'
						elif numberedBoard[boardIndex + y][lineIndex + x].isdigit():
							numberedBoard[boardIndex + y][lineIndex + x] = str(int(numberedBoard[boardIndex + y][lineIndex + x]) + 1)

	# convert the inner lists back into a single string
	for index in range(len(numberedBoard)):
		numberedBoard[index] = ''.join(numberedBoard[index])						
	return numberedBoard


