from graph import Graph

g = Graph()
for i in range(5):
	g.addVertex(str(i))
print(g.getVertices())
