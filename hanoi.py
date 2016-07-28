from rcviz import callgraph, viz

@viz
def hanoi(n, index, source, destination, temporary, alld):
	if n == 1:
		print ("Move " + alld[index] + " from " + source + "->" + destination)
	else:
		hanoi(n-1, index + 1, source, temporary, destination, alld)
		hanoi(1, index, source, destination, temporary, alld)
		hanoi(n -1, index + 1, temporary, destination, source, alld)

hanoi(4, 0, "Source", "Destination", "Temp", ["A", "B", "C", "D"])
callgraph.render("hanoi.png")