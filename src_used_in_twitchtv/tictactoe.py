import random

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
			getPlayerTurn(theBoard)
		else:
			# run the computer's turn
			getComputerTurn(theBoard)
		# did they win?
		# is there a tie?


def getPlayerTurn(bo):
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

		if bo[ALL_MOVES[int(response) - 1]] == EMPTY:
			print('That space is already taken.')
			continue


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
	pass #main()