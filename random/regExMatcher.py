'''
Build a regex Matcher for . (dot matches any single char) and * (asterix matches zero or more of the preceeding char). Given a string and a pattern(that contains dot and ansterix), output True or False if the string matches the pattern. Example : c*a*b matches aab and .* matches ab
'''

def recRegExMatch(s, pattern, ipat, ist):
	if ipat >= len(pattern) and ist >= len(s):
		return True
	if ipat < len(pattern)-1 and pattern[ipat+1] == '*':
		skip = False
		match = False
		match_letter = False
		skip = recRegExMatch(s, pattern, ipat+2, ist)
		if pattern[ipat] == '.':
			match = recRegExMatch(s, pattern, ipat, ist+1)
		else:
			if pattern[ipat] == s[ist]:
				match_letter = recRegExMatch(s, pattern, ipat, ist+1)
		return skip or match or match_letter
	else:
		if pattern[ipat] == s[ist]:
				return recRegExMatch(s, pattern, ipat+1, ist+1)
		else:
			return False




def regExMatch(s, pattern):
    return recRegExMatch(s, pattern, 0, 0)

print regExMatch("abcbcd", "a.*c.*d")