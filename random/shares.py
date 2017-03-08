from rcviz import callgraph, viz

#@viz
def _rec_shareTrading(stocks, index, qty, profit, cache):
	if index >= len(stocks):
		if not cache[index][qty]:
			cache[index][qty] = profit
		return cache[index][qty]
	else:
		current_profit = None
		
		#buy profit cached
		if not cache[index+1][qty+1]:
			cache[index+1][qty+1] = _rec_shareTrading(stocks, index+1, qty+1, profit - stocks[index],cache)
		buy_profit = cache[index+1][qty+1]

		#nothing profit cached
		if not cache[index+1][qty]:
			cache[index+1][qty] = _rec_shareTrading(stocks, index+1, qty, profit,cache)
		nothing_profit = cache[index+1][qty]

		current_profit = max(buy_profit, nothing_profit)
		
		#selling profit cached
		for q in xrange(1,qty+1):
			if not cache[index+1][qty-q]:
				cache[index+1][qty-q] = _rec_shareTrading(stocks, index+1, qty - q, (q*stocks[index])+ profit, cache)
			current_profit = max (current_profit, cache[index+1][qty-q])

		return current_profit


#@viz
def rec_shareTrading(stocks):
	#at index 0 you cant sell: only buy or do nothing
	cache = [[None] * (len(stocks)+1) for i in xrange(len(stocks)+1)]
	print cache

	cache[1][1] = _rec_shareTrading(stocks, 1, 1, -stocks[0], cache)
	cache[1][0] = _rec_shareTrading(stocks, 1, 0, 0, cache)

	#buy_profit = _rec_shareTrading(stocks, 1, 1, -stocks[0], cache)
	#nothing_profit = _rec_shareTrading(stocks, 1, 0, 0, cache)
	print cache
	return max(cache[1][1], cache[1][0])


print(rec_shareTrading([10, 7, 5, 8, 11, 9]))
#callgraph.render("shares.png")