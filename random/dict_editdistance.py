'''
Edit distance dicitonary problem: given a dictionary of words : {cat, bat, hat, bad, had} and two strings a, b: a = bat, b = had how to convert a->b by changing only 1 char at a time
'''

from graph import Graph

def edit_distance_dynamic_rec(source, target, i, j, cache):
    if i == len(source) and j == len(target):
        if cache[i][j] is not None:
            return cache[i][j]
        cache[i][j] = 0
        return cache[i][j]

    if i == len(source):
        if cache[i][j] is not None:
            return cache[i][j]
        #target has additional chars to add into source
        cache[i][j] = len(target) - j
        return cache[i][j]

    if j == len(target):
        if cache[i][j] is not None:
            return cache[i][j]
        #source has additional chars to delete
        cache[i][j] = len(source) - i
        return cache[i][j]

    else:
        if cache[i][j] is not None:
            return cache[i][j]
        if source[i] == target[j]:
            cache[i][j] = edit_distance_dynamic_rec(source, target, i+1, j+1, cache)
            return cache[i][j]
        else:
            cache[i][j] = 1 + min (edit_distance_dynamic_rec(source, target, i+1, j+1, cache),
                            edit_distance_dynamic_rec(source, target, i, j+1, cache),
                            edit_distance_dynamic_rec(source, target, i+1, j, cache))
            return cache[i][j]

def find_edit_distance(a, b):
    x = len(a) + 1
    y = len(b) + 1
    cache = [[None]*y for i in range(x)]
    return edit_distance_dynamic_rec(a, b, 0, 0, cache)

def buildGraphDictionary(words):
    g = Graph()
    for w in words:
        g.addVertex(w)
    for i in range(len(words)):
        source = words[i]
        for w in words:
            if source == w:
                pass
            else:
                if find_edit_distance(source, w) == 1:
                    g.addEdge(source, w, 1)
    #for vertex in g:
    #   for w in vertex.getConnections():
    #       print("( %s , %s )" % (vertex.getId(), w.getId()))
    return g

def findPaths(g, f, to, path, visited):
    if f == to:
        print(path + "->" + to)
        return
    if f in visited:
        return
    else:
        visited[f] = 1
        print(visited)
        fromV = g.getVertex(f)
        path = path + "->" + f
        for w in fromV.getConnections():
            nv = visited
            findPaths(g, w.getId(), to, path, nv)


words = ["cat", "bat", "hat", "bad", "had"]
g = buildGraphDictionary(words)
visited = {}
findPaths(g, "bat", "had", "", visited)

