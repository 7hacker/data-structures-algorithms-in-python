'''
nqueens problem
'''

def place(row, col, board):
	'''
	is placing on row,col possible without being attacked?
	board[row] contains col
	'''

	if board[-1] != None:
		return False

	for i in xrange(row):
		if board[i] == col:
			return False
		if abs(board[i]-col) == abs(i-row):
			return False
	return True

def _nqueens(row, board):
	if row >= len(board):
		return

	for i in xrange(len(board)):
		if place(row, i, board) == True:
			board[row] = i
			if row == len(board)-1:
				return
			else:
				_nqueens(row+1, board)

import sys
def printBoard(board):
	if board[-1] == None:
		print("No solution :")
	else:
		print("Found solution!:")
	for i in xrange(len(board)):
		sys.stdout.write("\n")
		for j in xrange(len(board)):
			if j == board[i]:
				sys.stdout.write(" Q ")
			else:
				sys.stdout.write(" - ")
	sys.stdout.write("\n")

def clearBoard(board):
	for i in xrange(len(board)):
		board[i] = None
	return


def nqueens(n):
	board = [None] * n
	done = False
	board[0] = 0
	while not done:
		_nqueens(1, board)
		printBoard(board)
		currentStart = board[0]
		if currentStart >= n-1:
			done = True
		else:
			clearBoard(board)
			board[0] = currentStart+1




nqueens(8)
