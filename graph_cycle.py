'''
detect if a graph has a cycle or not
'''
from graph import Graph

def visit(node):
	print("Visiting Node :" + str(node))
	return


def dfs(g, startAt, visited):
	startNode = g.getVertex(startAt)
	if not visited[startAt]:
		visit(startAt)
		visited[startAt] = 1
	for neighbor in startNode.getConnections():
		if not visited[neighbor.getId()]:
			visit(neighbor.getId())
			visited[neighbor.getId()] = 1
			dfs(g, neighbor.getId(), visited)
	return

def dfs_init(g, startAt):
	visited = [0] * len(g.getVertices())
	visit(startAt)
	visited[startAt] = 1
	dfs(g, startAt, visited)
	return

#Build a graph with a cycle
g = Graph()
for i in range(6):
	g.addVertex(i)
g.addEdge(0,2)
g.addEdge(0,5)
g.addEdge(0,4)
g.addEdge(4,0)
g.addEdge(4,5)
g.addEdge(2,5)
g.addEdge(2,1)
g.addEdge(1,0)
g.addEdge(3,1)
g.addEdge(3,6)
g.addEdge(6,3)
g.addEdge(6,5)

#Print the graph

for v in g:
	for w in v.getConnections():
		print(str(v.getId()) + "->" + str(w.getId()))

dfs_init(g, 3)
