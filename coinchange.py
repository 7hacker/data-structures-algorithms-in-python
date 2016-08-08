'''
Given N coins make change, C with the minimum number of coins. Output the coins used to make the Change. If there are more than one such sets, output them all. The same coin can be used repeatedly
'''
import sys
from rcviz import callgraph, viz

@viz
def coinchange(coins, amt, cache):
	if amt < 0:
		return 0
	if amt == 0:
		return cache[0]
	choices = 0
	for c in coins:
		if not cache[amt-c]:
			cache[amt-c] = coinchange(coins, amt-c, cache)
		choices= choices + cache[amt-c]
	return  choices



coins = [1,2,3]
amt = 4
cachesize = amt+1
cache = [None] * cachesize
cache[0] = 1
#cache = [[None] * (len(coins)) for i in range(amt+1)]
#cache[0][0] = 0
#print(cache)
print(coinchange(coins, amt, cache))
#print(cache)
callgraph.render("coinchange_dyn.png")

