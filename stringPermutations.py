'''
Write a recursive function for generating all permutations of an input string.  To start, assume every character in the input string is unique. 
'''
import sys

def recursivePerm(s, chosen):
	if len(chosen) == len(s):
		for c in chosen:
			sys.stdout.write(s[int(c)])
		sys.stdout.write("\n")
		return
	chosen_list = list()
	for c in chosen:
		chosen_list.append(c)
	i = 0
	while i < len(s):
		if str(i) in chosen_list:
			pass
		else:
			recursivePerm(s, chosen+str(i))
		i = i + 1


s = "abc"
i = 0
while i < len(s):
	recursivePerm(s, str(i))
	i = i + 1
