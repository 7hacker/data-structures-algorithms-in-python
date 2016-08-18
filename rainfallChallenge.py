'''
dat palantir Rain Fall Challenge
'''
import sys

class RainFallChallenge:
    
    def __init__(self, t):
        self.terrain = t
        self.size = len(t) #assume size x size terrain is passed
        self.basins = [[None]*self.size for i in xrange(self.size)]
        self.currentBasin = 64 #65 becomes 'A'

        #for x,y the neighbors are : x,y-1 x+1,y x,y+1 x-1,y
        self.neighborx = [0, 1, 0, -1] #clockwise from North 
        self.neighbory = [-1, 0, 1, 0]

        self._findSinks()
        self.showBasin()
        self._populateBasin(0,0)


    def isSafe(self, x, y):
        if x < self.size and y < self.size and x >=0 and y >=0: 
            return True
        else:
            return False

    def _findSinks(self):
        #find all the sinks. a sink is defined as being the lowest among its 4 neighbors
        for i in xrange(self.size):
            for j in xrange(self.size):
                vals = [self.terrain[i][j]]
                for k in xrange(4):
                    nx = i + self.neighborx[k]
                    ny = j + self.neighbory[k]
                    if self.isSafe(nx,ny):
                        vals.append(self.terrain[nx][ny])
                if min(vals) == self.terrain[i][j]:
                    #a new Basin can be formed, since a sink exists at this point
                    self.currentBasin = self.currentBasin+1
                    self.basins[i][j] = chr(self.currentBasin)

    def _mySmallestNeighbor(self, x, y):
        minVals = []
        d = {}
        for k in xrange(4):
            nx = x + self.neighborx[k]
            ny = y + self.neighbory[k]
            if self.isSafe(nx,ny):
                minVals.append(self.terrain[nx][ny])
                d[self.terrain[nx][ny]] = (nx, ny)
        mn = min(minVals)
        return d[mn]



    def _populateBasin(self, row, col):
        if row >= self.size or col >= self.size:
            #out of bounds
            return
        elif self.basins[row][col] != None:
            #i am already assigned a basin just move ahead
            if col+1 < self.size:
                self._populateBasin(row, col+1)
            else:
                self._populateBasin(row+1, 0)
            return
        else:
            (mnx, mny) = self._mySmallestNeighbor(row,col)
            if self.basins[mnx][mny] != None:
                self.basins[row][col] = self.basins[mnx][mny]
            else:
                self._populateBasin(mnx, mny)
                self.basins[row][col] = self.basins[mnx][mny]
            #recurse to next item
            if col+1 < self.size:
                self._populateBasin(row, col+1)
            else:
                self._populateBasin(row+1, 0)


    def showBasin(self):
        for i in xrange(self.size):
            sys.stdout.write("\n")
            for j in xrange(self.size):
                sys.stdout.write(str(self.basins[i][j]))
                sys.stdout.write(" ")
        sys.stdout.write("\n")


#t = [[1,5,2], [2,4,7], [3,6,9]]
t = [[1,0,2,5,8],[2,3,4,7,9],[3,5,7,8,9],[1,2,5,4,3],[3,3,5,2,1]]
rc = RainFallChallenge(t)
rc.showBasin()

