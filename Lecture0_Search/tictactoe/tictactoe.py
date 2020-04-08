"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

turn = None



def initial_state():
	"""
	Returns starting state of the board.
	"""
	return [[EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY]]


def player(board):
	"""
	Returns player who has the next turn on a board.
	"""
	if board == initial_state():
		return X

	numX=0
	numO=0

	for i in range(len(board)):
		for j in range(len(board)):
			if(board[i][j]==X):
				numX+=1
			elif(board[i][j]==O):
				numO+=1

	if numX > numO:
		return O
	else:
		return X					


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	poss_actions = set()
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j]==EMPTY:
				poss_actions.add((i,j))

	return poss_actions			



def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	newboard = copy.deepcopy(board)
	theturn = player(newboard)

	if newboard[action[0]][action[1]]!=EMPTY:
		raise ValueError
	else:
		if theturn==X:
			newboard[action[0]][action[1]]=X
		else:
			newboard[action[0]][action[1]]=O

	return newboard						
					

def checkForRow(row, player):
	for point in row:
		if point!=player:
			return False
	return True
	
def checkDiagonal(board,player):
	if(board[0][0] == player and board[1][1] == player and board[2][2]==player):
		return True
	if(board[2][0] == player and board[1][1] == player and board[0][2]==player):				
		return True
	return False	


def winnerForPlayer(board, player):
	for i in range(3):
		decision=checkForRow(board[i],player)
		if decision == True:
			return True

	for i in range(3):
		cols = [board[0][i], board[1][i], board[2][i]]
		decision=checkForRow(cols,player)
		if decision == True:
			return True


	if checkDiagonal(board,player) == True:
		return True

	return False	



def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	#For X
	iswinnerX = winnerForPlayer(board, X)
	iswinnerO = winnerForPlayer(board, O)

	if iswinnerX:
		return X
	if iswinnerO:
		return O

	return None		



def boardFull(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if(board[i][j])==EMPTY:
				return False
	return True			

def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	if boardFull(board)==True or winner(board)!=None:
		return True
	return False	


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	if winner(board) == X:
		return 1

	if winner(board) == O:
		return -1

	return 0		


def max_value(state):
    if terminal(state):
        return utility(state)
    v = float("-inf")
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    
    return v

def min_value(state):
    if terminal(state):
        return utility(state)
    v = float("inf")
    for action in actions(state):
        v = min(v, max_value(result(state, action)))

    return v	

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)

    if board == initial_state():
        return (0,0)

    if turn == X:
        v = float("-inf")
        current_action = None
        for action in actions(board):
            minVal = min_value(result(board, action))
            if minVal > v:
                v = minVal
                current_action = action
    elif turn == O:
        v = float("inf")
        current_action = None
        for action in actions(board):
            maxValueResult = max_value(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                current_action = action

    return current_action
    


