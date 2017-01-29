from rcviz import callgraph, viz


def fib_dyn(n,cache):
	for i in xrange(2,len(cache)):
		cache[i] = cache[i-1] + cache[i-2]
	return cache[len(cache)-1]


@viz
def fib_rec(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_rec(n-1) + fib_rec(n-2)

@viz
def fib_rec_cache(n,cache):
	if n ==0:
		return cache[0]
	if n == 1:
		return cache[1]

	fib_rec_cache.track(enter_cache_state=cache)
	
	if cache[n-1] == None:
		cache[n-1] = fib_rec_cache(n-1, cache)
	if cache[n-2] == None:
		cache[n-2] = fib_rec_cache(n-2, cache)
	
	cache[n] = cache[n-1] + cache[n-2]
	
	fib_rec_cache.track(exit_cache_state=cache)
	
	return cache[n]


#print fib_rec(7)
#print fib_rec_cache(n,cache)
n = 7
cache = [None] * (n+1)
cache[0] = 0
cache[1] = 1

print fib_dyn(n,cache)

#callgraph.render("fib-rec-cache.png")