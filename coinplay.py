'''
you and your friend are playing a game with coins, such that each coin has a value, and you can pick a coin from the start of a list or end of a list. If you begin first, and your friend is equally competent as you, what is the best choice you can make?
'''
from rcviz import callgraph, viz

@viz
def setAndFetch(coins, start, end, cache):
	if start >= len(cache) or end >= len(cache):
		return 0
	if not cache[start][end]:
		cache[start][end] = coin_play(coins, start, end, cache)
	return cache[start][end]


@viz
def coin_play(coins, start, end, cache):
	if start > end:
		return 0
	if start == end:
		return setAndFetch(coins, start, end, cache)
	else:
		choice1 = coins[start] + min(setAndFetch(coins, start+2, end, cache), setAndFetch(coins, start+1, end-1, cache))
		choice2 = coins[end] + min(setAndFetch(coins, start, end-2, cache), setAndFetch(coins, start+1, end-1, cache))
		return max(choice1, choice2)


coins = [149, 154, 63, 242, 12, 72, 65]
cache = [[None]*len(coins) for i in range(len(coins))]
print(coin_play(coins, 0, len(coins)-1, cache))
callgraph.render("coin_play.png")
