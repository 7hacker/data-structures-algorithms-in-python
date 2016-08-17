'''
Build a regex Matcher for . (dot matches any single char) and * (asterix matches zero or more of the preceeding char). Given a string and a pattern(that contains dot and ansterix), output True or False if the string matches the pattern. Example : c*a*b matches aab and .* matches ab
'''

def recRegExMatch(s, pattern, ipat, ist):
    if ipat > len(pattern) and ist > len(s):
        return True
    
    if pattern[ipat+1] == '*' and pattern[ipat] == s[ist]:
        return recRegExMatch(s, pattern, ipat+2, ist+1) or recRegExMatch(s, pattern, ipat, ist+1)
    else:
        return pattern[ipat] == s[ist] or regExMatch(s, pattern, ipat+1, ist+1)

def regExMatch(s, pattern):
    return recRegExMatch(s, pattern, 0, 0)

regExMatch("bbbc", "b*c")