def lcs_dyn(a,b):
	result = [[0] * (len(b)+1) for i in xrange(len(a)+1)]

	for i in xrange(len(a)+1):
		for j in xrange(len(b)+1):
			if i == 0 or j == 0:
				result[i][j] = 0
			else:
				if a[i-1] == b[j-1]:
					result[i][j] = 1 + result[i-1][j-1]
				else:
					result[i][j] = max(result[i-1][j], result[i][j-1])
	lcs = ""
	i = len(a)+1
	j = len(b)+1
	while i > 0 and j > 0:
		print(i)
		print(j)
		if a[i-1] == b[j-1]:
			lcs = lcs + a[i]
			i = i -1
			j = j -1
		elif result[i-1][j] > result[i][j-1]:
			i = i -1
		else:
			j = j - 1

	print(lcs)

	return result[-1][-1]




def _rec_lcs(a, b, ai, bi):
	if ai < 0 or bi < 0:
		return 0
	else:
		if a[ai] == b[bi]:
			return 1 + _rec_lcs(a, b, ai-1, bi-1)
		else:
			return max(_rec_lcs(a,b,ai-1, bi), _rec_lcs(a,b,ai, bi-1))


def rec_lcs(a, b):
	return _rec_lcs(a, b, len(a)-1, len(b)-1)

print(rec_lcs("AGGTAB", "GXTXAYB"))
print(lcs_dyn("AGGTAB", "GXTXAYB"))