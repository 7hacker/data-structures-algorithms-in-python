'''
snake & ladder game
'''
import sys

def shortest_throws(board, size):
    q = [(0,0, "0")]
    visited = [False] * size
    visited[0] = True
    while len(q):
        position, pathcost, pathstr = q.pop(0)
        if position == size - 1:
            return pathstr
        else:
            for i in xrange(1,7):
                newposition = position + i
                if newposition < size and not visited[newposition]:
                    visited[newposition] = True
                    if board[newposition] != -1:
                        newposition = board[newposition]
                    q.append((newposition, pathcost+1, pathstr+"->"+str(newposition)))




#set up a snake and ladder game
size = 30
board = [-1] * size
#Stairs
'''
board[2]  = 21;
board[4]  = 7;
board[10] = 25;
board[19] = 28;
    
#Snakes
board[16] = 3;
board[18] = 6;
board[20] = 8;
board[26] = 0;
'''
print shortest_throws(board, size)

