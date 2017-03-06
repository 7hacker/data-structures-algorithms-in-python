'''
A nice way to traverse matrices and operate on individual items
'''
import sys
def process(m, i, j):
	if j == 0:
		sys.stdout.write("\n")
	sys.stdout.write(str(m[i][j]) + " ")

def getnext(m, i, j):
	if j+1 < len(m[0]):
		return (i,j+1)
	else:
		return (i+1,0)

def trav(m):
	i = 0
	j = 0
	while i  < len(m):
		process(m, i,j)
		(i,j) = getnext(m, i, j)
	return

m = [
	[1,2,5,4],
	[100,200,500,400],
	[6,7,8,9],
	[11,3,7,13]
	]
trav(m)
