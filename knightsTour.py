'''
Knights tour
'''

import sys

class KT:
	def __init__(self, size):
		self.chessboard = [[None]*size for i in xrange(size)]
		self.size = size
		self.start = None
		self.kx = [1, 2, 2, 1, -1, -2, -2, -1]
		self.ky = [-2, -1, 1, 2, 2, 1, -1, -2]

	def setStart(self, x, y):
		if x < self.size and y < self.size:
			self.chessboard[x][y] = 0
			self.start = (x,y)

	def showBoard(self):
		for i in xrange(self.size):
			sys.stdout.write("\n")
			for j in xrange(self.size):
				sys.stdout.write(str(self.chessboard[i][j]))
				sys.stdout.write(" ")
		sys.stdout.write("\n")

	def isSafe(self, x, y):
		if x < self.size and y < self.size and x >= 0 and y >= 0:
			return True
		else:
			return False


	def _knightsTour(self, x, y, path):
		if self.chessboard[x][y] != None:
			return
		self.chessboard[x][y] = path
		for i in xrange(8):
			nx = x + self.kx[i]
			ny = y + self.ky[i]
			if self.isSafe(nx, ny) == True:
				self._knightsTour(nx, ny, path+1)


	def startKnightsTour(self):
		for i in xrange(8):
			nx = self.start[0] + self.kx[i]
			ny = self.start[1] + self.ky[i]
			if self.isSafe(nx, ny) == True:
				self._knightsTour(nx, ny, 1)


kt = KT(8)
kt.setStart(0, 0)
kt.startKnightsTour()
kt.showBoard()
