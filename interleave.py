from rcviz import callgraph, viz

@viz
def backtrack_interleave(s1, s2, i, j, match, n):
	if n == len(match):
		return True

	if i < len(s1) and s1[i] == match[n]:
		return backtrack_interleave(s1, s2, i+1, j, match, n+1)
	elif j < len(s2) and s2[j] == match[n]:
		return backtrack_interleave(s1, s2, i, j+1, match, n+1)
	else:
		return False


@viz
def rec_interleave(s, i, t, j, result, match):
	if len(result) == len(s) + len(t):
		return (result == match)

	elif i >= len(s):
		#exhaust t[j]
		return (rec_interleave(s, i, t, j+1, result + t[j], match) == True)
		
	elif j >= len(t):
		#exhaust s[i]
		return (rec_interleave(s, i+1, t, j, result + s[i], match) == True)
		
	else:
		return ((rec_interleave(s, i+1, t, j, result + s[i], match)) or (rec_interleave(s, i, t, j+1, result + t[j], match)))

@viz
def interleave(s1, s2, match):
	#return(rec_interleave(s1, 0, s2, 0, "", match))
	return backtrack_interleave(s1, s2, 0, 0, match, 0)

print(interleave("ab", "cd", "cadb"))
callgraph.render("interleave.png")
