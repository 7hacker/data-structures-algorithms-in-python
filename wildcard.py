from rcviz import callgraph, viz

@viz
def rec_wildcard(s, n, r):
	if n == len(s):
		print(r)
		return

	if s[n] == "?":
		rec_wildcard(s, n+1, r+"0")
		rec_wildcard(s, n+1, r+"1")
	else:
		rec_wildcard(s, n+1, r+s[n])

@viz
def wildcard(s):
	rec_wildcard(s,0, "")

wildcard("????")
callgraph.render("wildcard.png")