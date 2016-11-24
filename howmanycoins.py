from rcviz import callgraph, viz

@viz
def _coins(i , coins, n):
	if n == 0:
		return 1
	if i >= len(coins):
		return 0
	t = 0
	count = 0
	while (n - (t * coins[i]) >= 0):
		count = count + _coins(i+1, coins, n-(t * coins[i]))
		t = t + 1
	return count



@viz
def coins(n, c):
	'''return how many ways to make n change using coins from c'''
	count = 0
	t = 0
	while n - (t * c[0]) >= 0:
		count = count + _coins(1, c, n - (t * c[0]))
		t = t + 1
	return count
@viz
def _coins_cached(i, coins, n, cache):
	if n == 0:
		if not cache[i][n]:
			cache[i][n] = 1
		return cache[i][n]
	if i >= len(coins):
		return 0
	t = 0
	count = 0
	while n - (t * coins[i]) >= 0:
		if not cache[i][n - (t * coins[i])]:
			cache[i][n - (t * coins[i])] = _coins_cached(i+1, coins,n - (t * coins[i]), cache)
		count = count + cache[i][n - (t * coins[i])]
		t = t + 1
	return count

@viz
def coins_cached(n, coins, cache):
	count = 0
	t = 0
	while n - (t * coins[0]) >= 0:
		if not cache[0][n - (t * coins[0])]:
			cache[0][n - (t * coins[0])] = _coins_cached(1, coins, n - (t * coins[0]), cache)
		count = count + cache[0][n - (t * coins[0])]
		t = t + 1
	return count




n = 10
coins = [2, 5, 3, 6]
cache = [[None] * (n+1) for i in xrange(len(coins))]
print(cache)
#print(coins(n, coins))
print(coins_cached(n, coins, cache))
print(cache)
callgraph.render("howmanycoins_cached.png")

