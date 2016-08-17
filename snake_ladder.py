'''
snake & ladder game
'''
import sys

class Cell:
    def __init__(self, v, ladder, snake):
        self.v = v
        self.ladder = ladder
        self.snake = snake
        return

    def printCell(self):
        sys.stdout.write("Cell: " + str(self.v) )
        if self.ladder is not None:
            sys.stdout.write(" Ladder to: " + str(self.ladder))
        if self.snake is not None:
            sys.stdout.write(" Snake to: " + str(self.snake))
        sys.stdout.write("\n")
        return

    def getID(self):
        return self.v


class SnakeLadderGame:
    def __init__(self, size):
        self.board = [None] * size
        return

    def addCell(self, v, ladder, snake):
        c = Cell(v, ladder, snake)
        self.board[v]= c
        return

    def getLadder(self, cell):
        if cell.ladder is not None:
            return self.board[cell.ladder]
        else: 
            return None

    def getSnake(self, cell):
        if cell.snake is not None:
            return self.board[cell.snake]
        else:
            return None

    def printBoard(self):
        for cell in self.board:
            cell.printCell()
        return

    def getStartCell(self):
        return self.board[0]

    def isEndCell(self, c):
        return c.getID() == self.board[-1].getID()

    def isAfterEndCell(self, c):
        return c.getID > self.board[-1].getID()

    def moveCell(self, current, howmany):
        return self.board[current + howmany]


def findShortestGame(g, cell, moves):
    if g.isEndCell(cell):
        moves = moves + 1
        return moves
    if g.isAfterEndCell(cell):
        moves = sys.maxint
        return moves
    else:
        if l = g.getLadder(cell):
            cell = l
        if s = g.getSnake(cell):
            cell = s
        return min(
            findShortestGame(g, g.moveCell(cell.getID, 1), moves+1),
            findShortestGame(g, g.moveCell(cell.getID, 2), moves+1),
            findShortestGame(g, g.moveCell(cell.getID, 3), moves+1),
            findShortestGame(g, g.moveCell(cell.getID, 4), moves+1),
            findShortestGame(g, g.moveCell(cell.getID, 5), moves+1),
            findShortestGame(g, g.moveCell(cell.getID, 6), moves+1))

def shortestGame(g):
    startCell = g.getStartCell()
    print(findShortestGame(g, startCell,0))

g = SnakeLadderGame(5)
g.addCell(0, None, None)
g.addCell(1, 4, None)
g.addCell(2, None, 0)
g.addCell(3, None, None)
g.addCell(4, None, None)
#g.printBoard()
c = Cell(3, None, None)
print(g.isEndCell(c))
s = g.getStartCell()
s.printCell()
