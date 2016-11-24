'''
http://www.geeksforgeeks.org/find-all-strings-that-match-specific-pattern-in-a-dictionary/
'''

def encode(s):
	se = ""
	d = {}
	i = 0
	for c in s:
		if c not in d.keys():
			i = i + 1
			d[c] = i
		se = se + str(d[c])
	return se


def check_pattern(ls, p):
	encoded_pattern = encode(p)
	print(encoded_pattern)
	for item in ls:
		if encode(item) == encoded_pattern:
			print item

check_pattern(["abb", "abc", "xyz", "xyy"], "aba")

