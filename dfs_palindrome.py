from rcviz import callgraph, viz

@viz
def isPalin(s):
	l = 0
	r = len(s)-1
	while l < r:
		if s[l] != s[r]:
			return False
		else:
			l = l +1 
			r = r -1
	return True

@viz
def addpalindrome(s, start, partition, result):
	if start == len(s):
		temp = list(partition)
		result.append(temp)
		return
	else:
		for i in xrange(start+1, len(s)+1):
			substr = s[start:i]
			if isPalin(substr):
				partition.append(substr)
				addpalindrome.track(palindrome=substr) 
				addpalindrome.track(partition=partition) 

				addpalindrome(s, i, partition, result)
				partition.pop()
				addpalindrome.track(removedpartition=partition) 

@viz
def partition(s):
	result = []
	if not s or len(s) == 0:
		return result
	else:
		partition = []
		addpalindrome(s, 0, partition, result)
		return result

print partition("madam")
callgraph.render("dfspalindrome.png")