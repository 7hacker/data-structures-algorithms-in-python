'''
cut a rope of size n such that the product of the cuts is maximized atleast one cut must be made example: rope of size = 4 the best cut is 2,2 (2 * 2 = 4) as opposed to 3,1 (3* 1 = 3) or 1,3 or 1,2,1, 2,1,1, 1,1,1,1
'''

def rope_cut(size, cache):
	if size <= 1:
		return cache[size]
	else:
		maxp = 0
		k = 1
		for i in xrange(size-1, -1, -1):
			if not cache[i]:
				cache[i] = k * rope_cut(i,cache)
			maxp = max(maxp, cache[i])
			k = k + 1
		cache[size] = maxp
		return cache[size]


n = 5
cache = [None] * (n+1)
cache[0] = 1
cache[1] = 1
print cache
print(rope_cut(n, cache))
print cache