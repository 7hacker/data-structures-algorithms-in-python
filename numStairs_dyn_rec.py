from rcviz import callgraph, viz

@viz
def numStairs_rec(n, m, cache):
    if n == 0:
        cache[0] = 1
        return cache[0]
    elif n < 0:
        return 0
    else:
        
        if cache[n] != 0:
            return cache[n]
        else:
            total = 0
            for step in m:
                total = total + numStairs_rec(n-step, m, cache)
            cache[n] = total
            return cache[n]

@viz
def  numWaysToClimb(numSteps, numStairs):
    cachesize = numStairs + 1
    cache = [0] * cachesize
    return numStairs_rec(numStairs, numSteps, cache)

print(numWaysToClimb([3,4,7], 14))
callgraph.render("numStairs_dyn.png")