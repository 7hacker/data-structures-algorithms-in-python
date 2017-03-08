'''
How many ways can you climb N stairs, if you can take some [I, J, K...] steps? : Exhaustive
'''
from rcviz import callgraph, viz

@viz
def numStairs_rec(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        for step in m:
            total = total + numStairs_rec(n-step, m)
        return total

@viz
def  numWaysToClimb(numSteps, numStairs):
    return numStairs_rec(numStairs, numSteps)


print(numWaysToClimb([3,4,7], 14))
callgraph.render("numStairs_exhaustive.png")