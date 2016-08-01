'''
detect if a graph has a cycle or not
'''
from graph import Graph

def visit(node):
	print("Visiting Node :" + str(node))
	return


def detectCycle(g):
	'''
	#using clrs method of finding cycles by marking nodes by colors:
	white(0) indicates this node was never seen
	gray(1) indicates this node is currently being processed
	black(2) indicates this node is done
	if in a dfs visit a gray node is encoutnered a cycle is found
	https://algocoding.wordpress.com/2015/04/02/detecting-cycles-in-a-directed-graph-with-dfs-python/comment-page-1/
	'''
	color = {}
	for v in g.getVertices():
		color[v] = 0 #set to white
	found_cycle = [False]
	for v in g.getVertices():
		if not color[v]: #if node is white
			findCycle(g, v, color, found_cycle)
		if found_cycle[0]:
			break
	return found_cycle[0]


def findCycle(g, v, color, found_cycle):
	if found_cycle[0]:
		return True
	color[v] = 1 #set to gray
	vNode = g.getVertex(v)
	for neighbor in vNode.getConnections():
		if color[neighbor.getId()] == 1 :
			found_cycle[0] = True
			return
		if color[neighbor.getId()] == 0:
			findCycle(g, neighbor.getId(), color, found_cycle)
	color[v] = 2 #set to black since you are done


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

#Build a graph
g = Graph()
for i in range(6):
	g.addVertex(i)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(0,4)
g.addEdge(0,5)

#Print the graph
for v in g:
	for w in v.getConnections():
		print(str(v.getId()) + "->" + str(w.getId()))

print(detectCycle(g))
#dfs_init(g, 3)
