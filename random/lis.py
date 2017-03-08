def lis_dyn(a):
	cache = [None] * len(a)
	cache[-1] = 1
	for i in xrange(len(a)-2, -1, -1):
		max_lis = 0
		for k in range(i+1, len(a)):
			if a[k] > a[i]:
				max_lis = max(max_lis, cache[k])
		cache[i] = max_lis + 1
	return max(cache)

def _lis_rec(a, i,cache):
	if i == len(a)-1:
		if not cache[i]:
			cache[i] = 1
		return cache[i]
	max_lis = 0
	for k in xrange(i+1, len(a)):
		if a[k] > a[i]:
			if not cache[k]:
				cache[k] = _lis_rec(a,k,cache)
			max_lis = max(max_lis, cache[k])
	return 1 + max_lis

def lis_rec(a):
	cache = [None] * len(a)
	max_lis = 0
	for k in xrange(len(a)):
		if not cache[k]:
			cache[k] = _lis_rec(a,k,cache)
		max_lis = max(max_lis, cache[k])
	return max_lis

print lis_rec([2, 7, 4, 3, 8])
print lis_dyn([2, 7, 4, 3, 8])