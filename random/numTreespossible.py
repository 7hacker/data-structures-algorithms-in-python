'''
how many structurally unique binary trees are possible with n nodes?
'''
from rcviz import callgraph, viz

@viz
def numTreesPossible(n, cache):
	if n == 0:
		return cache[0]
	elif n == 1:
		return cache[1]
	else:
		answer = 0
		k = 1
		while n-k >= 0:

			if not cache[n-k]:
				cache[n-k] = numTreesPossible(n-k, cache)
			left_answer = cache[n-k]

			if not cache[k-1]:
				cache[k-1] = numTreesPossible(k-1, cache)
			right_answer = cache[k-1]

			answer = answer + (left_answer * right_answer)		
			
			k = k + 1
		return answer


n = 4
cache = [0] * (n+1)
cache[0] = 1
cache[1] = 1
print numTreesPossible(n, cache)
callgraph.render("numTreesPossible_cached.png")