'''
Build a regex Matcher for . (dot matches any single char) and * (asterix matches zero or more of the preceeding char). Given a string and a pattern(that contains dot and ansterix), output True or False if the string matches the pattern
'''

from stack import Stack

def regExMatch(s, pattern):
	st = Stack()
	i = 0
	while i < len(pattern)-1:
		if pattern[i+1] == '.' or pattern[i+1] == '*':
			st.push(pattern[i]+pattern[i+1])
			i = i + 2
		else:
			st.push(pattern[i])
			i = i + 1
	if pattern[-1] != '.' and pattern[-1] != '*':
		st.push(pattern[-1])

	rs = s[::-1]
	print(rs)
	#st.show()

regExMatch("abc", "a*b.c")