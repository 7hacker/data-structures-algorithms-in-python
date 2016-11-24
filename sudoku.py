
import sys
def print_board(b):
	for i in xrange(9):
		for j in xrange(9):
			if b[i][j]:
				sys.stdout.write(str(b[i][j]) + " ")
			else:
				sys.stdout.write("- ")
		sys.stdout.write("\n")
	sys.stdout.write("\n")


def make_board(s):
	board = [[None] * 9 for i in xrange(9)]
	k = 0
	for i in xrange(9):
		for j in xrange(9):
			if s[k] != ".":
				board[i][j] = int(s[k])
			k = k + 1
	return board

def getBox(i, j):
	startx = None
	starty = None
	if i >=0 and i < 3:
		startx = 0
	elif i >= 3 and i < 6:
		startx = 3
	else:
		startx = 6

	if j >=0 and j < 3:
		starty = 0
	elif j >= 3 and j < 6:
		starty = 3
	else:
		starty = 6

	return (startx, starty)


def get_candidates(b, startx, starty):
	#make a sudoku candidate dic
	sd = {}
	for i in xrange(1, 10):
		sd[i] = True

	#check row
	for i in xrange(9):
		if b[startx][i] in sd:
			del sd[b[startx][i]]

	#check col
	for i in xrange(9):
		if b[i][starty] in sd:
			del sd[b[i][starty]]

	#check box
	(topLeftx, topLefty) = getBox(startx, starty)
	for i in xrange(topLeftx, topLeftx+3):
		for j in xrange(topLefty, topLefty+3):
			if b[i][j] in sd:
				del sd[b[i][j]]

	return sd.keys()


def find_next_blank_cell(b, x, y):
	#find along the row first:
	for i in xrange(y, 9):
		if b[x][i] == None:
			return (x, i)
	#nothing was found in the x row
	for i in xrange(x+1, 9):
		for j in xrange(9):
			if b[i][j] == None:
				return (i,j)

	return (None,None)


def solve_sudoku_bt(b, startx, starty):
	
	(bx, by) = find_next_blank_cell(b, startx, starty)

	if bx == None and by == None:
		return True
	else:
		candidates = get_candidates(b, bx, by)
		for c in candidates:
			b[bx][by] = c
			if solve_sudoku_bt(b, bx, by) == True:
				return True
			else:
				b[bx][by] = None
		return False



def solve_all_puzzles(f):
	fo = open(f, "r")
	frl = fo.readlines()

	for l in frl:
		b = make_board(l)
		if solve_sudoku_bt(b, 0, 0):
			print "Solved! "
			print_board(b)
		else:
			print "Not Solved: "
			print_board(b)

solve_all_puzzles("sudoku_input_file")