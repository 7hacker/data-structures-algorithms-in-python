'''
 "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis). 
'''

def soln(s, n):
	if s[n] != "(":
		return None
	else:
		count = 1
		for i in xrange(n+1, len(s)):
			if s[i] == "(":
				count = count + 1
			elif s[i] == ")":
				count = count - 1
				if count == 0:
					return i
		return None

print(soln("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10))
