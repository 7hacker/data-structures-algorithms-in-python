'''
print all subsets of a given array/list
'''
from rcviz import callgraph, viz

@viz
def rec_printAllSubsets(unselected, selected, n):
	if n < len(unselected):
		rec_printAllSubsets(unselected, selected, n+1)
		rec_printAllSubsets(unselected, selected + " " + str(unselected[n]), n+ 1)
	else:
		print("{" + selected + " }")
		return 


@viz
def printAllSubsets(l):
	rec_printAllSubsets(l, "", 0)

printAllSubsets([1,2,3])
callgraph.render("subsets.png")
