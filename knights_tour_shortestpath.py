'''
You are given two inputs: starting location and ending location. The goal is to then calculate and print the shortest path that the knight can take to get to the target location.
'''

import sys

class KT:
	def __init__(self, size):
		self.chessboard = [[None]*size for i in xrange(size)]
		self.size = size
		self.kx = [1, 2, 2, 1, -1, -2, -2, -1]
		self.ky = [-2, -1, 1, 2, 2, 1, -1, -2]

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


	def shortestPath(self, startx, starty, endx, endy):
		#check if the destination is within limits
		if not self.isSafe(endx, endy):
			return -1
		#use BFS:
		q = []
		if startx == endx and starty == endy :
			return 0
		q.append((startx, starty, 0))
		while len(q):
			(x, y, path) = q.pop(0)
			if x == endx and y == endy:
				return path
			for i in xrange(8):
				nx = x + self.kx[i]
				ny = y + self.ky[i]
				if self.isSafe(nx, ny):
					q.append((nx, ny, path+1))

		return -1




kt = KT(8)
#kt.showBoard()
print(kt.shortestPath(0 , 0, 1, 0))
#kt.showBoard()



