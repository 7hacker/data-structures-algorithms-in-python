'''
What houses must a robber steal from, to get max value, if houses are indicated by value and adjacent houses cannot be stolen
'''
from rcviz import callgraph, viz

def robber_iterative(houses, cache):
	best = max(houses[len(houses) -1], houses[len(houses) -2])
	cache[len(houses) -1 ] = best
	cache[len(houses) -2 ] = best
	for i in range(len(houses) -3, -1, -1):
		cache[i] = max(houses[i] + cache[i+2], cache[i+1])
	return cache[0]


def robber(houses, start):
	if start >= len(houses):
		if cache[start] == None:
			cache[start] = 0
		return cache[start]
	else:

		if cache[start+2] == None:
			cache[start+2] = robber(houses, start+2) + houses[start]
		stolen = cache[start+2]
		
		if cache[start+1] == None:
			cache[start+1] = robber(houses, start+1)
		notStolen = cache[start+1]

		return max(stolen, notStolen)


houses = [6,1,2,7]
cache_size = len(houses)
cache = [0] * cache_size
#print(robber(houses, 0))
print(robber_iterative(houses, cache))