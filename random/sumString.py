'''
http://www.geeksforgeeks.org/calculate-sum-of-all-numbers-present-in-a-string/
'''


def sumString(s):
	sv = 0
	i = j = 0
	while i < len(s) and j < len(s):
		if s[i].isdigit():
			j = i + 1
			while j < len(s) and s[j].isdigit():
				j = j + 1
			sv = sv + int(s[i:j])
			i = j
		else:
			i = i + 1
	return sv

print sumString("100nima100")
