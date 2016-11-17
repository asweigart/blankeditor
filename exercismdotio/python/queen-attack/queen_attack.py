def can_attack(whiteQueenPos, blackQueenPos):
    if whiteQueenPos == blackQueenPos:
        raise ValueError('White and black queen are on the same space.')
    if whiteQueenPos[0] < 0 or whiteQueenPos[0] > 7 or whiteQueenPos[1] < 0 or whiteQueenPos[1] > 7:
        raise ValueError('White queen is on an invalid space.')
    if blackQueenPos[0] < 0 or blackQueenPos[0] > 7 or blackQueenPos[1] < 0 or blackQueenPos[1] > 7:
        raise ValueError('Black queen is on an invalid space.')

    if whiteQueenPos[0] == blackQueenPos[0] or whiteQueenPos[1] == blackQueenPos[1]:
        return True


    for xdirection, ydirection in ((1, 1), (-1, -1), (1, -1), (-1, 1)):
        x, y = whiteQueenPos
        while x >= 0 and y >= 0 and x < 8 and y < 8:
            x += xdirection
            y += ydirection
            if (x, y) == blackQueenPos:
                return True
    return False



def board(whiteQueenPos, blackQueenPos):
    if whiteQueenPos == blackQueenPos:
        raise ValueError('White and black queen are on the same space.')
    if whiteQueenPos[0] < 0 or whiteQueenPos[0] > 7 or whiteQueenPos[1] < 0 or whiteQueenPos[1] > 7:
        raise ValueError('White queen is on an invalid space.')
    if blackQueenPos[0] < 0 or blackQueenPos[0] > 7 or blackQueenPos[1] < 0 or blackQueenPos[1] > 7:
        raise ValueError('Black queen is on an invalid space.')

    board = [['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_'],
             ['_', '_', '_', '_', '_', '_', '_', '_']]

    board[whiteQueenPos[0]][whiteQueenPos[1]] = 'W'
    board[blackQueenPos[0]][blackQueenPos[1]] = 'B'

    for index, innerList in enumerate(board):
        board[index] = ''.join(innerList)

    return board
