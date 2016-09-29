import random
import copy

TOPLEFT = 'topleft'
TOPMIDDLE = 'topmiddle'
TOPRIGHT = 'topright'
MIDDLELEFT = 'middleleft'
MIDDLEMIDDLE = 'middlemiddle'
MIDDLERIGHT = 'middleright'
BOTTOMLEFT = 'bottomleft'
BOTTOMMIDDLE = 'bottommiddle'
BOTTOMRIGHT = 'bottomright'

ALL_MOVES = [TOPLEFT, TOPMIDDLE, TOPRIGHT, 
			 MIDDLELEFT, MIDDLEMIDDLE, MIDDLERIGHT, 
			 BOTTOMLEFT, BOTTOMMIDDLE, BOTTOMRIGHT]
X = 'X'
O = 'O'
EMPTY = ' '

PLAYER_TURN = 'player'
COMPUTER_TURN = 'computer'

def main():
	print('Welcome to Tic Tac Toe!')

	# get player's mark
	playerMark = getPlayerMark()
	if playerMark == X:
		computerMark = O
	else:
		computerMark = X

	# decide who goes first
	turn = getFirstPlayer()

	# create a brand new blank tic tac toe board
	theBoard = getBlankBoard()

	while True:
		# display the board
		displayBoard(theBoard)
		
		# run player/computer's turn
		if turn == PLAYER_TURN:
			# run the player's turn
			move = getPlayerMove(theBoard) # move is one of the space constants like TOPLEFT
			theBoard[move] = playerMark

			# did they win?
			if isWinner(theBoard, playerMark):
				print('You have won!!!!!!1111')
				return
			turn = COMPUTER_TURN
		else:
			# run the computer's turn
			move = getComputerMove(theBoard, computerMark)
			theBoard[move] = computerMark

			# did they win?
			if isWinner(theBoard, computerMark):
				print('The computer has beaten you!')
				return
			turn = PLAYER_TURN

		# is there a tie?
		isTie = True
		for move in ALL_MOVES:
			if theBoard[move] == EMPTY:
				isTie = False
		if isTie:
			print('The game is a tie!')
			return



def getPlayerMove(bo):
	# ask the player to enter a move on the board.
	# the space must be empty
	print('1|2|3')
	print('-+-+-')
	print('4|5|6')
	print('-+-+-')
	print('7|8|9')

	while True:
		print('Enter the number of your move:')
		response = input()
		if response not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			print('Please enter a number from 1 to 9.')
			continue

		if bo[ALL_MOVES[int(response) - 1]] != EMPTY:
			print('That space is already taken.')
			continue

		return ALL_MOVES[int(response) - 1]

def isWinner(bo, mark):
	return bo[TOPLEFT] == bo[TOPMIDDLE] == bo[TOPRIGHT] == mark or  \
	       bo[MIDDLELEFT] == bo[MIDDLEMIDDLE] == bo[MIDDLERIGHT] == mark or  \
	       bo[BOTTOMLEFT] == bo[BOTTOMMIDDLE] == bo[BOTTOMRIGHT] == mark or  \
	       bo[TOPLEFT] == bo[MIDDLELEFT] == bo[BOTTOMLEFT] == mark or  \
	       bo[TOPMIDDLE] == bo[MIDDLEMIDDLE] == bo[BOTTOMMIDDLE] == mark or  \
	       bo[TOPRIGHT] == bo[MIDDLERIGHT] == bo[BOTTOMRIGHT] == mark or  \
	       bo[TOPLEFT] == bo[MIDDLEMIDDLE] == bo[BOTTOMRIGHT] == mark or \
	       bo[TOPRIGHT] == bo[MIDDLEMIDDLE] == bo[BOTTOMLEFT] == mark 



def getComputerMove(bo, computerMark):
	if computerMark == X:
		playerMark = O
	else:
		playerMark = X

	# check for winning move and make it
	for move in ALL_MOVES:
		duplicateBo = copy.copy(bo)

		if duplicateBo[move] != EMPTY:
			continue
		duplicateBo[move] = computerMark
		if isWinner(duplicateBo, computerMark):
			return move

	# check if human player is going to win, and block it
	for move in ALL_MOVES:
		duplicateBo = copy.copy(bo)

		if duplicateBo[move] != EMPTY:
			continue
		duplicateBo[move] = playerMark
		if isWinner(duplicateBo, playerMark):
			return move	

	# move on a corner space (if available)
	emptyCornerSpaces = []
	for possiblyEmptySpace in [TOPLEFT, TOPRIGHT, BOTTOMLEFT, BOTTOMRIGHT]:
		if possiblyEmptySpace == EMPTY:
			emptyCornerSpaces.append(possiblyEmptySpace)
	if len(emptyCornerSpaces) > 0:
		return random.choice(emptyCornerSpaces)

	# move on center space (if available)
	if bo[MIDDLEMIDDLE] == EMPTY:
		return MIDDLEMIDDLE
	
	# move on a side space
	emptySideSpaces = []
	for possiblyEmptySpace in [TOPMIDDLE, MIDDLELEFT, MIDDLERIGHT, BOTTOMMIDDLE]:
		if possiblyEmptySpace == EMPTY:
			emptySideSpaces.append(possiblyEmptySpace)

	return random.choice(emptySideSpaces)



def getPlayerMark():
	# prompts the player if they want to be "X" or "O"
	while True:
		print('Do you want to be X or O?')
		response = input()
		response = response.upper()
		if response == X or response == O:
			return response



def getFirstPlayer():
	return random.choice([PLAYER_TURN, COMPUTER_TURN])


def getBlankBoard():
	# returns a blank ttt board for a new game
	return {TOPLEFT:      EMPTY,
			TOPMIDDLE:    EMPTY,
			TOPRIGHT:     EMPTY,
			MIDDLELEFT:   EMPTY,
			MIDDLEMIDDLE: EMPTY,
			MIDDLERIGHT:  EMPTY,
			BOTTOMLEFT:   EMPTY,
			BOTTOMMIDDLE: EMPTY,
			BOTTOMRIGHT:  EMPTY}

def displayBoard(bo):
	# displays the board data structure that is passed in as `bo`
	print('   |   |   ')
	print(' %s | %s | %s ' % (bo[TOPLEFT], bo[TOPMIDDLE], bo[TOPRIGHT]))
	print('   |   |   ')
	print('---|---|---')
	print('   |   |   ')
	print(' %s | %s | %s ' % (bo[MIDDLELEFT], bo[MIDDLEMIDDLE], bo[MIDDLERIGHT]))
	print('   |   |   ')
	print('---|---|---')
	print('   |   |   ')
	print(' %s | %s | %s ' % (bo[BOTTOMLEFT], bo[BOTTOMMIDDLE], bo[BOTTOMRIGHT]))
	print('   |   |   ')


if __name__ == '__main__':
	main()