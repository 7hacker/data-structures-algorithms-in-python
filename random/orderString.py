'''
https://www.careercup.com/question?id=5659201272545280
'''

def OrderExists(s,p):
	d = {}
	v = 1
	for c in p:
		d[c] = v
		v = v + 1
	
	v = 0
	for c in s:
		if c in d.keys():
			if d[c] < v:
				return False
			if d[c] == v + 1:
				v = v + 1
	if v == len(d.keys()):
		return True
	else:
		return False


print(OrderExists("aaaabbbcccc", "ac"))


