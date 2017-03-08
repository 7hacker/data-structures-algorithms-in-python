'''
given a sentence like this: "Coding for Interviews contains too many gifs." Returns the sentence with the order of the words reversed, like so: "gifs. many too contains Interviews for Coding" The catch was: your function should use O(1) space.
'''

def inplace_rev(s, start, end):
	print(s)
	while start < end:
		t = s[start]
		s[start] = s[end]
		s[end] = t
		start = start + 1
		end = end - 1
	print(s)


def soln(s):
	sl = []
	for c in s:
		sl.append(c)
	
	starti = 0
	endi = 0
	
	while endi <= len(sl):
		while sl[endi] != " ":
			endi = endi + 1
		inplace_rev(sl, starti, endi)
		starti = endi
		endi = endi + 1


	inplace_rev(sl, 0, len(sl)-1)

soln("nirmal is awesome!")
#def soln(s):
