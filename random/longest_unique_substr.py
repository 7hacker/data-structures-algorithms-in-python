'''
length of the longest unique substring in a given string
'''
def longest_unique(s):
	hs = set()
	start = 0
	end = 1
	hs.add(s[start])
	while end < len(s):
		if s[end] not in hs:
			hs.add(s[end])
			end = end + 1
		else:
			while s[end] in hs:
				hs.remove(s[start])
				start = start + 1
			hs.add(s[end])
			end = end + 1
	print hs
	return len(hs)

print longest_unique("abccdefgh")