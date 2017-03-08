'''
print out all permutations of a given string & print out all the subsets formed by characters of a given string
'''
def _rec_permute(s, remaining):
	if len(remaining) == 0:
		print "".join(s)
	else:
		i = 0
		while i < len(remaining):
			s.append(remaining.pop(0))
			_rec_permute(s, remaining)
			remaining.append(s.pop())
			i = i + 1
	
def rec_permute(s):
	result = []
	remainder =[]
	for c in s:
		remainder.append(c)
	i = 0
	while i < len(s):
		result.append(remainder.pop(0))
		_rec_permute(result,remainder)
		remainder.append(result.pop(0))
		i = i + 1

def _rec_subset(s, i, result):
	if i >= len(s):
		print(result)
	else:
		_rec_subset(s, i + 1, result)
		result.append(s[i])
		_rec_subset(s, i + 1, result)
		result.pop()


def rec_subset(s):
	res = []
	return _rec_subset(s, 0, res)


rec_permute("dog")
rec_subset("dog")