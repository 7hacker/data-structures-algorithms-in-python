
def showcache(c):
	import sys
	for i in xrange(len(c)):
		sys.stdout.write("\n")
		for j in xrange(len(c)):
			sys.stdout.write(str(c[i][j])+ " ")
	sys.stdout.write("\n")


def longestPalinSize(s):
	cache = [[0] * len(s) for i in xrange(len(s))]

	for i in xrange(len(s)-1, -1, -1):
		for j in xrange(i, len(s)):
			if i == j:
				cache[i][j] = 1
			else:
				if s[i] == s[j] and (cache[i+1][j-1] or j-i <= 2):
					cache[i][j] = 1
	showcache(cache)
	maxcount = 0

	for i in xrange(len(s)):
		for j in xrange(i,len(s)):
			if cache[i][j]:
				maxcount = max(maxcount, j-1)

	return maxcount


print longestPalinSize("Neveroddoreven")